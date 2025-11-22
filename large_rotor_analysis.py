#!/usr/bin/env python3
"""
Test with very large rotors to minimize power requirements
Key insight: Larger propellers = lower disk loading = much less power needed
"""

from simulator import *


def test_large_rotors():
    """Test configurations with very large propellers"""
    print("="*80)
    print("LARGE ROTOR CONFIGURATION ANALYSIS")
    print("="*80)
    print("\nKey insight: Power ∝ 1/sqrt(disk_area)")
    print("Doubling prop size reduces power by ~30%\n")

    payload_kg = lbs_to_kg(240)

    # Test configurations with increasingly large props
    configs = [
        # (num_rotors, diameter_inches, gen_kw)
        (8, 30, 20),  # 8 × 30"
        (8, 36, 18),  # 8 × 36" (very large)
        (8, 42, 16),  # 8 × 42" (huge!)
        (6, 36, 18),  # 6 × 36"
        (6, 42, 16),  # 6 × 42"
        (6, 48, 14),  # 6 × 48" (massive!)
        (4, 48, 16),  # 4 × 48" (quadcopter with huge props)
        (4, 54, 14),  # 4 × 54" (extreme)
    ]

    print(f"{'Configuration':<20} {'Disk Area':<12} {'Aircraft':<12} {'Peak Power':<12} {'Ratio':<10} {'Status':<10}")
    print("-"*90)

    viable_designs = []

    for num_rotors, diameter_in, gen_kw in configs:
        diameter_m = diameter_in * 0.0254

        # Weight estimates (larger props = heavier motors)
        motor_weight_each = 0.2 + (diameter_in / 30) * 0.3
        total_motor_weight = num_rotors * motor_weight_each

        # Frame weight (less arms = lighter)
        if num_rotors <= 4:
            frame_weight = 2.0
        elif num_rotors <= 6:
            frame_weight = 2.5
        else:
            frame_weight = 3.5

        # Generator weight (rough estimate: 0.6 kg per kW above 10 kW)
        gen_weight_kg = 7.0 + max(0, gen_kw - 10) * 0.6

        # Other components
        electronics = 1.0
        landing_gear = 0.8
        payload_mount = 0.5

        airframe_weight_kg = (frame_weight + total_motor_weight +
                             electronics + landing_gear + payload_mount)

        total_aircraft_kg = airframe_weight_kg + gen_weight_kg
        total_aircraft_lbs = kg_to_lbs(total_aircraft_kg)

        # Skip if over weight
        if total_aircraft_lbs > 55:
            disk_area = num_rotors * math.pi * (diameter_m/2)**2
            config_name = f"{num_rotors} × {diameter_in}\""
            print(f"{config_name:<20} {disk_area:<11.2f}m² {total_aircraft_lbs:<11.1f}lbs {'N/A':<12} {'N/A':<10} ✗ Over 55 lbs")
            continue

        # Create configuration
        config = AircraftConfig(
            aircraft_weight_kg=airframe_weight_kg,
            num_rotors=num_rotors,
            rotor_diameter_m=diameter_m,
            hover_efficiency=0.65,
            cruise_efficiency=0.75,
            has_wing=False,
            hybrid_power=True,
            generator_weight_kg=gen_weight_kg,
            generator_power_w=gen_kw * 1000,
            battery_capacity_wh=0,
            battery_weight_kg=0
        )

        # Analyze performance
        result = payload_ratio_analysis(config, payload_kg)

        disk_area = config.total_disk_area()
        peak_power_kw = result['max_power_w'] / 1000

        # Check feasibility
        power_ok = peak_power_kw < gen_kw * 1.1  # 10% margin
        time_ok = result['meets_time_requirement']

        viable = power_ok and time_ok

        status = "✓ VIABLE" if viable else "✗ No"

        config_name = f"{num_rotors} × {diameter_in}\" ({gen_kw}kW)"
        print(f"{config_name:<20} {disk_area:<11.2f}m² {total_aircraft_lbs:<11.1f}lbs {peak_power_kw:<11.1f}kW {result['payload_ratio']:<9.2f} {status:<10}")

        if viable:
            viable_designs.append({
                'config_str': f"{num_rotors} × {diameter_in}\"",
                'gen_kw': gen_kw,
                'aircraft_lbs': total_aircraft_lbs,
                'ratio': result['payload_ratio'],
                'peak_power_kw': peak_power_kw,
                'disk_area_m2': disk_area,
                'time_min': result['mission_time_min'],
                'energy_kwh': result['mission_energy_wh'] / 1000,
                'config': config,
                'result': result
            })

    if viable_designs:
        print("\n" + "="*80)
        print("VIABLE DESIGNS FOUND!")
        print("="*80)

        # Sort by payload ratio
        viable_designs.sort(key=lambda x: x['ratio'], reverse=True)

        for i, design in enumerate(viable_designs, 1):
            print(f"\n### Option {i}: {design['config_str']} with {design['gen_kw']} kW generator ###")
            print(f"  Aircraft weight: {design['aircraft_lbs']:.1f} lbs")
            print(f"  Payload ratio: {design['ratio']:.2f}:1")
            print(f"  Disk area: {design['disk_area_m2']:.1f} m²")
            print(f"  Peak power: {design['peak_power_kw']:.1f} kW")
            print(f"  Mission time: {design['time_min']:.1f} min")
            print(f"  Mission energy: {design['energy_kwh']:.1f} kWh")

        return viable_designs
    else:
        print("\n✗ NO VIABLE DESIGNS FOUND")
        print("\nThis suggests 240 lb payload may not be achievable within 55 lb limit")
        print("with current hybrid generator technology.")
        return []


def test_lower_payloads():
    """Find what payload IS achievable"""
    print("\n" + "="*80)
    print("FINDING ACHIEVABLE PAYLOAD TARGETS")
    print("="*80)

    # Reasonable configuration: 8 rotors × 30", 15 kW generator
    print("\n### Using 8 Rotors × 30\" with 15 kW Generator ###\n")

    # Lightweight config
    airframe_weight_kg = 7.0  # Frame + motors + electronics
    gen_weight_kg = 10.0  # 15 kW generator

    config = AircraftConfig(
        aircraft_weight_kg=airframe_weight_kg,
        num_rotors=8,
        rotor_diameter_m=0.76,  # 30 inches
        hover_efficiency=0.65,
        cruise_efficiency=0.75,
        has_wing=False,
        hybrid_power=True,
        generator_weight_kg=gen_weight_kg,
        generator_power_w=15000,
        battery_capacity_wh=0,
        battery_weight_kg=0
    )

    aircraft_lbs = kg_to_lbs(config.total_weight())
    print(f"Aircraft weight: {aircraft_lbs:.1f} lbs")
    print(f"Disk area: {config.total_disk_area():.2f} m²\n")

    print(f"{'Payload (lbs)':<15} {'Ratio':<10} {'Peak Power':<15} {'Time (min)':<12} {'Feasible':<10}")
    print("-"*70)

    max_viable_payload = 0
    max_viable_ratio = 0

    for payload_lbs in range(110, 260, 10):
        payload_kg = lbs_to_kg(payload_lbs)

        result = payload_ratio_analysis(config, payload_kg)

        power_ok = result['max_power_w'] < 15000 * 1.15  # 15% margin
        time_ok = result['meets_time_requirement']

        viable = power_ok and time_ok
        status = "✓" if viable else "✗"

        print(f"{payload_lbs:<15} {result['payload_ratio']:<9.2f} {result['max_power_w']/1000:<14.1f}kW {result['mission_time_min']:<11.1f} {status:<10}")

        if viable:
            max_viable_payload = payload_lbs
            max_viable_ratio = result['payload_ratio']

    print(f"\n**Maximum viable payload: {max_viable_payload} lbs**")
    print(f"**Maximum payload ratio: {max_viable_ratio:.2f}:1**")

    return max_viable_payload


if __name__ == "__main__":
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "LARGE ROTOR VIABILITY ANALYSIS" + " "*27 + "║")
    print("╚" + "="*78 + "╝")
    print()

    viable_large_rotor_designs = test_large_rotors()

    max_achievable = test_lower_payloads()

    print("\n" + "="*80)
    print("CONCLUSIONS")
    print("="*80)

    if viable_large_rotor_designs:
        print("\n✓ 240 lb payload IS ACHIEVABLE with large propellers!")
        print(f"\nBest design: {viable_large_rotor_designs[0]['config_str']}")
        print(f"Requires: {viable_large_rotor_designs[0]['gen_kw']} kW generator")
        print(f"Achieves: {viable_large_rotor_designs[0]['ratio']:.2f}:1 payload ratio")
    else:
        print("\n✗ 240 lb payload appears VERY DIFFICULT with 55 lb aircraft limit")
        print(f"\nMore realistic target: {max_achievable} lbs")
        print("\nChallenge: Generator weight scales with power requirement")
        print("          Heavy payloads need high power, which needs heavy generators")

    print("\n" + "="*80)
