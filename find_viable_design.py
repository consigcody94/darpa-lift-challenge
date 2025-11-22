#!/usr/bin/env python3
"""
Find the minimum viable design that meets 240 lb payload target
"""

from simulator import *
import math


def find_required_generator_power():
    """Determine minimum generator size for 240 lb payload"""
    print("="*80)
    print("FINDING MINIMUM GENERATOR SIZE FOR 240 LB PAYLOAD")
    print("="*80)

    payload_kg = lbs_to_kg(240)

    # Test with 16 rotors, 24" props
    config_base = {
        'aircraft_weight_kg': 11.0,
        'num_rotors': 16,
        'rotor_diameter_m': 0.61,
        'hover_efficiency': 0.65,
        'cruise_efficiency': 0.75,
        'has_wing': False,
        'hybrid_power': True,
    }

    print("\n### Testing 16 Rotors × 24\" Props ###\n")

    for gen_power_kw in range(15, 35, 5):
        gen_weight_kg = 8 + (gen_power_kw - 10) * 0.5  # Estimate: ~0.5 kg per additional kW

        config = AircraftConfig(
            **config_base,
            generator_weight_kg=gen_weight_kg,
            generator_power_w=gen_power_kw * 1000,
            battery_capacity_wh=0,
            battery_weight_kg=0
        )

        aircraft_lbs = kg_to_lbs(config.total_weight())

        if aircraft_lbs > 55:
            print(f"{gen_power_kw} kW: Aircraft {aircraft_lbs:.1f} lbs - ✗ Over weight limit")
            continue

        result = payload_ratio_analysis(config, payload_kg)

        power_ok = result['max_power_w'] < gen_power_kw * 1000 * 1.1  # 10% margin

        status = "✓" if power_ok else "✗"

        print(f"{gen_power_kw} kW generator ({gen_weight_kg:.1f} kg):")
        print(f"  Aircraft: {aircraft_lbs:.1f} lbs")
        print(f"  Peak power: {result['max_power_w']/1000:.1f} kW")
        print(f"  Payload ratio: {result['payload_ratio']:.2f}:1")
        print(f"  Status: {status}")
        print()

        if power_ok:
            print(f"**MINIMUM GENERATOR: {gen_power_kw} kW**\n")
            return gen_power_kw, gen_weight_kg

    return None, None


def find_optimal_rotor_config_for_payload(target_payload_lbs):
    """Find best rotor configuration for target payload"""
    print("="*80)
    print(f"OPTIMIZING ROTOR CONFIGURATION FOR {target_payload_lbs} LB PAYLOAD")
    print("="*80)

    payload_kg = lbs_to_kg(target_payload_lbs)

    best_config = None
    best_ratio = 0

    # Test various configurations
    configs_to_test = [
        {'name': '16 rotors × 24"', 'rotors': 16, 'diameter_m': 0.61, 'gen_kw': 30},
        {'name': '16 rotors × 28"', 'rotors': 16, 'diameter_m': 0.71, 'gen_kw': 25},
        {'name': '20 rotors × 24"', 'rotors': 20, 'diameter_m': 0.61, 'gen_kw': 25},
        {'name': '24 rotors × 22"', 'rotors': 24, 'diameter_m': 0.56, 'gen_kw': 25},
        {'name': '12 rotors × 30"', 'rotors': 12, 'diameter_m': 0.76, 'gen_kw': 25},
    ]

    print(f"\n{'Configuration':<25} {'Aircraft (lbs)':<15} {'Peak Power':<15} {'Ratio':<10} {'Viable':<10}")
    print("-"*80)

    for test in configs_to_test:
        # Estimate weights
        motor_weight_per = 0.3 + (test['diameter_m'] - 0.5) * 0.4
        total_motor_weight = test['rotors'] * motor_weight_per

        frame_weight = 2.0 + (test['rotors'] / 8) * 1.0  # Scales with complexity

        gen_weight = 8 + (test['gen_kw'] - 10) * 0.5

        electronics = 1.2
        landing_gear = 1.0
        payload_mount = 0.5

        airframe_kg = frame_weight + total_motor_weight + electronics + landing_gear + payload_mount

        config = AircraftConfig(
            aircraft_weight_kg=airframe_kg,
            num_rotors=test['rotors'],
            rotor_diameter_m=test['diameter_m'],
            hover_efficiency=0.65,
            cruise_efficiency=0.75,
            has_wing=False,
            hybrid_power=True,
            generator_weight_kg=gen_weight,
            generator_power_w=test['gen_kw'] * 1000,
            battery_capacity_wh=0,
            battery_weight_kg=0
        )

        aircraft_lbs = kg_to_lbs(config.total_weight())

        if aircraft_lbs > 55:
            print(f"{test['name']:<25} {aircraft_lbs:<14.1f} {'N/A':<15} {'N/A':<10} ✗ Too heavy")
            continue

        result = payload_ratio_analysis(config, payload_kg)

        power_ok = result['max_power_w'] < test['gen_kw'] * 1000 * 1.1
        time_ok = result['meets_time_requirement']

        viable = power_ok and time_ok

        status = "✓" if viable else "✗"

        print(f"{test['name']:<25} {aircraft_lbs:<14.1f} {result['max_power_w']/1000:<14.1f}kW {result['payload_ratio']:<9.2f} {status:<10}")

        if viable and result['payload_ratio'] > best_ratio:
            best_ratio = result['payload_ratio']
            best_config = {
                'name': test['name'],
                'config': config,
                'result': result,
                'aircraft_lbs': aircraft_lbs
            }

    if best_config:
        print(f"\n**BEST CONFIGURATION: {best_config['name']}**")
        print(f"  Aircraft: {best_config['aircraft_lbs']:.1f} lbs")
        print(f"  Payload ratio: {best_config['result']['payload_ratio']:.2f}:1")
        print(f"  Peak power: {best_config['result']['max_power_w']/1000:.1f} kW")
        print(f"  Mission time: {best_config['result']['mission_time_min']:.1f} min")

    return best_config


def create_final_design_recommendation():
    """Create final, validated design recommendation"""
    print("\n" + "="*80)
    print("FINAL DESIGN RECOMMENDATION (Physics-Validated)")
    print("="*80)

    # Test three payload targets
    targets = [110, 200, 240]

    for target in targets:
        print(f"\n### TARGET: {target} LBS PAYLOAD ###\n")
        best = find_optimal_rotor_config_for_payload(target)
        print()


if __name__ == "__main__":
    # First, find minimum generator size
    min_gen_kw, min_gen_kg = find_required_generator_power()

    print("\n")

    # Then find optimal configurations for different targets
    create_final_design_recommendation()
