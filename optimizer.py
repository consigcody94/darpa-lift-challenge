#!/usr/bin/env python3
"""
DARPA Lift Challenge - Design Optimizer

Finds optimal aircraft configurations by varying key parameters.
Identifies designs that maximize payload ratio while meeting mission requirements.
"""

import math
from simulator import *
import json


def optimize_rotor_configuration(target_payload_kg: float,
                                max_aircraft_weight_kg: float,
                                hybrid_generator_weight_kg: float,
                                hybrid_generator_power_w: float,
                                has_wing: bool = False) -> Dict:
    """
    Find optimal rotor size and count for a given payload target.

    Args:
        target_payload_kg: Target payload weight
        max_aircraft_weight_kg: Maximum allowed aircraft weight
        hybrid_generator_weight_kg: Weight of hybrid generator
        hybrid_generator_power_w: Continuous power output of generator
        has_wing: Does this design have a wing?

    Returns: Best configuration found
    """
    print(f"\n{'='*80}")
    print(f"OPTIMIZING for {target_payload_kg:.0f} kg ({kg_to_lbs(target_payload_kg):.0f} lbs) payload")
    print(f"{'='*80}")

    best_config = None
    best_ratio = 0
    results = []

    # Test different configurations
    rotor_counts = [4, 6, 8, 12, 16] if not has_wing else [4, 6, 8]
    rotor_diameters = [0.35, 0.40, 0.46, 0.51, 0.56, 0.61, 0.66, 0.71, 0.76]  # 14" to 30" in meters

    for num_rotors in rotor_counts:
        for rotor_diameter_m in rotor_diameters:
            rotor_diameter_inches = rotor_diameter_m / 0.0254

            # Estimate airframe weight based on number of rotors and size
            # Larger frames and more rotors = more weight
            if has_wing:
                # Quadplane: wing + fuselage + rotors
                base_frame_weight = 2.5 + (num_rotors * 0.3) + 3.5  # Wing adds ~3.5 kg
                wing_area = 1.2 if num_rotors <= 6 else 1.5
            else:
                # Multirotor: just frame + motors
                base_frame_weight = 1.5 + (num_rotors * 0.25)
                wing_area = 0.0

            # Motor weight scales with size
            motor_weight_per = 0.25 + (rotor_diameter_m - 0.35) * 0.5
            total_motor_weight = num_rotors * motor_weight_per

            # Electronics, landing gear, payload mount
            electronics_weight = 1.0
            landing_gear_weight = 0.8
            payload_mount_weight = 0.5

            # Total airframe weight (excluding generator)
            airframe_weight_kg = (base_frame_weight + total_motor_weight +
                                electronics_weight + landing_gear_weight +
                                payload_mount_weight)

            # Total aircraft weight
            total_aircraft_kg = airframe_weight_kg + hybrid_generator_weight_kg

            # Skip if over weight limit
            if total_aircraft_kg > max_aircraft_weight_kg:
                continue

            # Create configuration
            config = AircraftConfig(
                aircraft_weight_kg=airframe_weight_kg,
                num_rotors=num_rotors,
                rotor_diameter_m=rotor_diameter_m,
                hover_efficiency=0.65,
                cruise_efficiency=0.75,
                has_wing=has_wing,
                wing_area_m2=wing_area,
                wing_efficiency=0.85,
                hybrid_power=True,
                generator_weight_kg=hybrid_generator_weight_kg,
                generator_power_w=hybrid_generator_power_w,
                battery_capacity_wh=0,  # Not relevant for hybrid
                battery_weight_kg=0
            )

            # Calculate performance
            try:
                analysis = payload_ratio_analysis(config, target_payload_kg)

                # Check if generator is adequate
                if analysis['max_power_w'] > hybrid_generator_power_w * 1.2:  # Allow 20% overpower briefly
                    continue

                # Check if mission time is feasible
                if not analysis['meets_time_requirement']:
                    continue

                # Check if we have good time margin (at least 3 minutes)
                if analysis['time_margin_min'] < 3.0:
                    continue

                # This is a valid configuration
                result = {
                    'num_rotors': num_rotors,
                    'rotor_diameter_m': rotor_diameter_m,
                    'rotor_diameter_in': rotor_diameter_inches,
                    'aircraft_weight_kg': total_aircraft_kg,
                    'aircraft_weight_lbs': kg_to_lbs(total_aircraft_kg),
                    'payload_ratio': analysis['payload_ratio'],
                    'mission_time_min': analysis['mission_time_min'],
                    'time_margin_min': analysis['time_margin_min'],
                    'peak_power_w': analysis['max_power_w'],
                    'avg_power_w': analysis['avg_power_w'],
                    'energy_wh': analysis['mission_energy_wh'],
                    'disk_area_m2': config.total_disk_area(),
                    'disk_loading_kg_m2': config.disk_loading(total_aircraft_kg + target_payload_kg)
                }

                results.append(result)

                # Track best
                if analysis['payload_ratio'] > best_ratio:
                    best_ratio = analysis['payload_ratio']
                    best_config = result

            except Exception as e:
                # Skip invalid configurations
                continue

    # Sort results by payload ratio
    results.sort(key=lambda x: x['payload_ratio'], reverse=True)

    return {
        'best': best_config,
        'top_10': results[:10],
        'all_valid': results
    }


def compare_designs():
    """Compare different design approaches"""
    print("\n" + "="*80)
    print("DESIGN COMPARISON ANALYSIS")
    print("="*80)

    target_payload = lbs_to_kg(240)  # 240 lbs
    max_aircraft_weight = lbs_to_kg(55)  # 55 lbs limit

    # Test 1: Pure octocopter with various generator sizes
    print("\n### SCENARIO 1: Octocopter with different generators ###")

    generators = [
        {'name': 'Small (3kW)', 'weight': 4.0, 'power': 3000},
        {'name': 'Medium (5kW)', 'weight': 7.0, 'power': 5000},
        {'name': 'Large (8kW)', 'weight': 10.0, 'power': 8000},
        {'name': 'X-Large (12kW)', 'weight': 13.0, 'power': 12000},
    ]

    for gen in generators:
        print(f"\n--- {gen['name']} Generator ---")
        print(f"Generator: {gen['weight']:.1f} kg, {gen['power']}W")

        result = optimize_rotor_configuration(
            target_payload_kg=target_payload,
            max_aircraft_weight_kg=max_aircraft_weight,
            hybrid_generator_weight_kg=gen['weight'],
            hybrid_generator_power_w=gen['power'],
            has_wing=False
        )

        if result['best']:
            best = result['best']
            print(f"\n✓ FEASIBLE")
            print(f"  Best: {best['num_rotors']} rotors × {best['rotor_diameter_in']:.0f}\"")
            print(f"  Aircraft weight: {best['aircraft_weight_lbs']:.1f} lbs")
            print(f"  PAYLOAD RATIO: {best['payload_ratio']:.2f}:1")
            print(f"  Mission time: {best['mission_time_min']:.1f} min (margin: {best['time_margin_min']:.1f} min)")
            print(f"  Peak power: {best['peak_power_w']/1000:.1f} kW")
            print(f"  Energy: {best['energy_wh']/1000:.1f} kWh")
            print(f"  Disk loading: {best['disk_loading_kg_m2']:.1f} kg/m²")
        else:
            print(f"✗ NO FEASIBLE SOLUTION FOUND")

    # Test 2: Quadplane with wing
    print("\n\n### SCENARIO 2: Quadplane (Hybrid VTOL) ###")

    for gen in generators[:3]:  # Test smaller generators for quadplane
        print(f"\n--- {gen['name']} Generator ---")
        print(f"Generator: {gen['weight']:.1f} kg, {gen['power']}W")

        result = optimize_rotor_configuration(
            target_payload_kg=lbs_to_kg(220),  # Slightly lower target for quadplane
            max_aircraft_weight_kg=max_aircraft_weight,
            hybrid_generator_weight_kg=gen['weight'],
            hybrid_generator_power_w=gen['power'],
            has_wing=True
        )

        if result['best']:
            best = result['best']
            print(f"\n✓ FEASIBLE")
            print(f"  Best: {best['num_rotors']} rotors × {best['rotor_diameter_in']:.0f}\"")
            print(f"  Aircraft weight: {best['aircraft_weight_lbs']:.1f} lbs")
            print(f"  PAYLOAD RATIO: {best['payload_ratio']:.2f}:1")
            print(f"  Mission time: {best['mission_time_min']:.1f} min (margin: {best['time_margin_min']:.1f} min)")
            print(f"  Peak power: {best['peak_power_w']/1000:.1f} kW")
            print(f"  Energy: {best['energy_wh']/1000:.1f} kWh")
        else:
            print(f"✗ NO FEASIBLE SOLUTION FOUND")


def sensitivity_analysis():
    """Analyze sensitivity to key parameters"""
    print("\n" + "="*80)
    print("SENSITIVITY ANALYSIS")
    print("="*80)

    # Base configuration (octocopter with 12kW generator)
    base_config = AircraftConfig(
        aircraft_weight_kg=11.0,  # Airframe only
        num_rotors=16,
        rotor_diameter_m=0.61,
        hover_efficiency=0.65,
        cruise_efficiency=0.75,
        has_wing=False,
        hybrid_power=True,
        generator_weight_kg=13.0,
        generator_power_w=12000,
        battery_capacity_wh=0,
        battery_weight_kg=0
    )

    baseline_payload = lbs_to_kg(240)

    print("\n### Baseline Configuration ###")
    baseline = payload_ratio_analysis(base_config, baseline_payload)
    print(f"16 rotors × 24\" diameter")
    print(f"Aircraft: {baseline['aircraft_weight_lbs']:.1f} lbs")
    print(f"Payload ratio: {baseline['payload_ratio']:.2f}:1")
    print(f"Mission time: {baseline['mission_time_min']:.1f} min")
    print(f"Peak power: {baseline['max_power_w']/1000:.1f} kW")
    print(f"Energy: {baseline['mission_energy_wh']/1000:.1f} kWh")

    # Vary hover efficiency
    print("\n### Sensitivity to Hover Efficiency ###")
    for efficiency in [0.55, 0.60, 0.65, 0.70, 0.75]:
        config = AircraftConfig(
            aircraft_weight_kg=11.0,
            num_rotors=16,
            rotor_diameter_m=0.61,
            hover_efficiency=efficiency,
            cruise_efficiency=0.75,
            has_wing=False,
            hybrid_power=True,
            generator_weight_kg=13.0,
            generator_power_w=12000
        )
        result = payload_ratio_analysis(config, baseline_payload)
        print(f"  η={efficiency:.2f}: Power={result['max_power_w']/1000:.1f}kW, "
              f"Energy={result['mission_energy_wh']/1000:.1f}kWh, "
              f"Time={result['mission_time_min']:.1f}min")

    # Vary number of rotors (keeping total disk area similar)
    print("\n### Sensitivity to Rotor Count (constant disk area) ###")
    base_area = base_config.total_disk_area()

    for num_rotors in [8, 12, 16, 20]:
        # Calculate diameter to maintain same total area
        diameter_m = math.sqrt(4 * base_area / (num_rotors * math.pi))
        diameter_in = diameter_m / 0.0254

        config = AircraftConfig(
            aircraft_weight_kg=11.0,
            num_rotors=num_rotors,
            rotor_diameter_m=diameter_m,
            hover_efficiency=0.65,
            cruise_efficiency=0.75,
            has_wing=False,
            hybrid_power=True,
            generator_weight_kg=13.0,
            generator_power_w=12000
        )
        result = payload_ratio_analysis(config, baseline_payload)
        print(f"  {num_rotors} × {diameter_in:.1f}\": Power={result['max_power_w']/1000:.1f}kW, "
              f"Time={result['mission_time_min']:.1f}min")


if __name__ == "__main__":
    # Run optimization
    compare_designs()

    print("\n")
    sensitivity_analysis()

    print("\n" + "="*80)
    print("Optimization complete!")
    print("="*80)
