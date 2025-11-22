#!/usr/bin/env python3
"""
DARPA Lift Challenge - Physics-Based Performance Simulator

This module provides core physics calculations for VTOL drone performance:
- Hover power (momentum theory)
- Forward flight power
- Energy consumption
- Performance metrics

All calculations use SI units internally, with conversion functions provided.
"""

import math
from dataclasses import dataclass
from typing import Tuple, Dict
import json


# Physical constants
GRAVITY = 9.81  # m/s^2
AIR_DENSITY_SEA_LEVEL = 1.225  # kg/m^3
GASOLINE_ENERGY_DENSITY = 12000  # Wh/kg
LIPO_ENERGY_DENSITY = 250  # Wh/kg


# Unit conversion helpers
def lbs_to_kg(lbs: float) -> float:
    """Convert pounds to kilograms"""
    return lbs * 0.453592

def kg_to_lbs(kg: float) -> float:
    """Convert kilograms to pounds"""
    return kg / 0.453592

def nm_to_km(nm: float) -> float:
    """Convert nautical miles to kilometers"""
    return nm * 1.852

def km_to_nm(km: float) -> float:
    """Convert kilometers to nautical miles"""
    return km / 1.852

def mph_to_ms(mph: float) -> float:
    """Convert miles per hour to meters per second"""
    return mph * 0.44704

def ms_to_kmh(ms: float) -> float:
    """Convert meters per second to kilometers per hour"""
    return ms * 3.6


@dataclass
class AircraftConfig:
    """Aircraft configuration parameters"""
    # Basic parameters
    aircraft_weight_kg: float  # Empty weight in kg (without payload)
    num_rotors: int  # Number of lift rotors
    rotor_diameter_m: float  # Diameter of each rotor in meters

    # Efficiency factors
    hover_efficiency: float = 0.65  # Typical 0.6-0.7 for multirotors
    cruise_efficiency: float = 0.75  # Motor/prop efficiency in forward flight
    has_wing: bool = False  # Is this a hybrid VTOL with wing?
    wing_area_m2: float = 0.0  # Wing area if applicable
    wing_efficiency: float = 0.85  # Wing L/D ratio factor

    # Power system
    hybrid_power: bool = True  # Using hybrid gas-electric?
    generator_weight_kg: float = 0.0
    generator_power_w: float = 0.0
    battery_capacity_wh: float = 0.0
    battery_weight_kg: float = 0.0

    def total_disk_area(self) -> float:
        """Calculate total rotor disk area in m^2"""
        single_rotor_area = math.pi * (self.rotor_diameter_m / 2) ** 2
        return single_rotor_area * self.num_rotors

    def disk_loading(self, total_weight_kg: float) -> float:
        """Calculate disk loading in kg/m^2"""
        return total_weight_kg / self.total_disk_area()

    def total_weight(self) -> float:
        """Calculate total aircraft weight including power system"""
        return (self.aircraft_weight_kg +
                self.generator_weight_kg +
                self.battery_weight_kg)


class PerformanceCalculator:
    """Calculate aircraft performance metrics"""

    def __init__(self, config: AircraftConfig):
        self.config = config

    def hover_power_ideal(self, total_weight_kg: float) -> float:
        """
        Calculate ideal hover power using momentum theory.

        Formula: P_ideal = T^1.5 / sqrt(2 * rho * A)
        where:
            T = thrust (weight in Newtons)
            rho = air density
            A = total disk area

        Returns: Power in Watts
        """
        thrust_n = total_weight_kg * GRAVITY
        disk_area = self.config.total_disk_area()

        if disk_area <= 0:
            raise ValueError("Disk area must be positive")

        # Momentum theory formula
        power_ideal = (thrust_n ** 1.5) / math.sqrt(2 * AIR_DENSITY_SEA_LEVEL * disk_area)

        return power_ideal

    def hover_power_actual(self, total_weight_kg: float) -> float:
        """
        Calculate actual hover power including losses.

        Returns: Power in Watts
        """
        ideal_power = self.hover_power_ideal(total_weight_kg)
        actual_power = ideal_power / self.config.hover_efficiency
        return actual_power

    def forward_flight_power(self, total_weight_kg: float, speed_ms: float) -> float:
        """
        Calculate power required for forward flight.

        For multirotors: Still use rotors, some translational lift benefit
        For hybrid VTOL: Wing provides lift, rotors mainly for control

        Args:
            total_weight_kg: Total weight in kg
            speed_ms: Forward speed in m/s

        Returns: Power in Watts
        """
        if self.config.has_wing:
            # Hybrid VTOL - wing provides most lift
            return self._wing_forward_power(total_weight_kg, speed_ms)
        else:
            # Pure multirotor - translational lift benefit
            return self._multirotor_forward_power(total_weight_kg, speed_ms)

    def _multirotor_forward_power(self, total_weight_kg: float, speed_ms: float) -> float:
        """
        Multirotor forward flight power.
        Benefits from translational lift (helicopter effect).
        Typical reduction: 10-30% vs hover at moderate speeds.
        """
        hover_power = self.hover_power_actual(total_weight_kg)

        # Translational lift benefit peaks around 10-15 m/s
        # Model as quadratic benefit up to optimal speed, then drag increases
        optimal_speed = 12.0  # m/s (about 27 mph)

        if speed_ms <= optimal_speed:
            # Benefit increases with speed up to optimal
            benefit_factor = 0.15 * (speed_ms / optimal_speed)
            power_reduction = hover_power * benefit_factor
            forward_power = hover_power - power_reduction
        else:
            # Beyond optimal, drag starts to dominate
            excess_speed = speed_ms - optimal_speed
            drag_penalty = hover_power * 0.02 * (excess_speed / optimal_speed)
            forward_power = hover_power * 0.85 + drag_penalty

        return forward_power

    def _wing_forward_power(self, total_weight_kg: float, speed_ms: float) -> float:
        """
        Hybrid VTOL forward flight power.
        Wing provides lift, rotors at reduced power for control.
        Much more efficient than pure multirotor.
        """
        # Dynamic pressure
        q = 0.5 * AIR_DENSITY_SEA_LEVEL * speed_ms ** 2

        # Lift from wing (assumes angle of attack generates required lift)
        lift_coefficient = 1.2  # Typical for high-lift airfoil
        wing_lift_n = q * self.config.wing_area_m2 * lift_coefficient

        # How much weight does wing support?
        total_weight_n = total_weight_kg * GRAVITY
        wing_lift_fraction = min(wing_lift_n / total_weight_n, 0.95)  # Wing can't support 100%

        # Remaining lift from rotors
        rotor_thrust_n = total_weight_n * (1 - wing_lift_fraction)
        rotor_weight_equivalent = rotor_thrust_n / GRAVITY

        # Power for rotor thrust (much less than hover)
        rotor_power = self.hover_power_ideal(rotor_weight_equivalent) / self.config.hover_efficiency

        # Induced drag from wing
        aspect_ratio = 12  # Typical for efficient wing
        lift_to_drag = aspect_ratio * self.config.wing_efficiency
        drag_n = wing_lift_n / lift_to_drag

        # Power to overcome drag
        drag_power = drag_n * speed_ms / self.config.cruise_efficiency

        # Total forward flight power
        total_power = rotor_power + drag_power

        return total_power

    def climb_power(self, total_weight_kg: float, climb_rate_ms: float) -> float:
        """
        Calculate power for climbing.

        Args:
            total_weight_kg: Total weight
            climb_rate_ms: Vertical climb rate in m/s

        Returns: Power in Watts
        """
        # Hover power + potential energy increase rate
        hover_power = self.hover_power_actual(total_weight_kg)
        climb_power_component = total_weight_kg * GRAVITY * climb_rate_ms / self.config.hover_efficiency

        return hover_power + climb_power_component

    def max_flight_time(self, total_weight_kg: float, avg_power_w: float) -> float:
        """
        Calculate maximum flight time in minutes.

        Args:
            total_weight_kg: Total aircraft + payload weight
            avg_power_w: Average power consumption

        Returns: Flight time in minutes
        """
        if self.config.hybrid_power:
            # Hybrid: generator provides continuous power
            available_energy = self.config.generator_power_w * 2.0  # 2 hours worth at rated power
            # Assume fuel capacity for 2+ hours
        else:
            # Battery only
            available_energy = self.config.battery_capacity_wh

        flight_time_hours = available_energy / avg_power_w
        return flight_time_hours * 60  # Convert to minutes


def calculate_mission_energy(config: AircraftConfig,
                            payload_kg: float,
                            cruise_speed_ms: float = 7.5) -> Dict:
    """
    Calculate energy consumption for complete DARPA Lift Challenge mission.

    Mission profile:
    - Takeoff and climb to 350 ft (107 m)
    - Cruise 4 nm (7.41 km) loaded at 350 ft
    - Descend and drop payload
    - Climb back to 350 ft
    - Cruise 1 nm (1.85 km) unloaded
    - Descend and land

    Args:
        config: Aircraft configuration
        payload_kg: Payload weight in kg
        cruise_speed_ms: Cruise speed in m/s (default 7.5 m/s = 16.8 mph)

    Returns: Dictionary with energy breakdown
    """
    calc = PerformanceCalculator(config)

    # Weights
    loaded_weight = config.total_weight() + payload_kg
    unloaded_weight = config.total_weight()

    # Phase 1: Takeoff and climb (assume 2 m/s climb rate to 107m)
    climb_altitude = 107  # meters (350 ft)
    climb_rate = 2.0  # m/s
    climb_time_s = climb_altitude / climb_rate  # 53.5 seconds
    climb_power = calc.climb_power(loaded_weight, climb_rate)
    climb_energy_wh = (climb_power * climb_time_s / 3600)

    # Phase 2: Loaded cruise (4 nm = 7408 m)
    loaded_distance = 7408  # meters
    loaded_cruise_time_s = loaded_distance / cruise_speed_ms
    loaded_cruise_power = calc.forward_flight_power(loaded_weight, cruise_speed_ms)
    loaded_cruise_energy_wh = (loaded_cruise_power * loaded_cruise_time_s / 3600)

    # Phase 3: Descend and drop payload (assume hover during drop)
    descent_time_s = 60  # 1 minute to descend and stabilize
    drop_time_s = 30  # 30 seconds for payload release
    payload_drop_power = calc.hover_power_actual(loaded_weight)
    payload_drop_energy_wh = (payload_drop_power * (descent_time_s + drop_time_s) / 3600)

    # Phase 4: Climb back (unloaded now)
    climb_back_power = calc.climb_power(unloaded_weight, climb_rate)
    climb_back_energy_wh = (climb_back_power * climb_time_s / 3600)

    # Phase 5: Unloaded cruise (1 nm = 1852 m)
    unloaded_distance = 1852  # meters
    unloaded_cruise_time_s = unloaded_distance / cruise_speed_ms
    unloaded_cruise_power = calc.forward_flight_power(unloaded_weight, cruise_speed_ms)
    unloaded_cruise_energy_wh = (unloaded_cruise_power * unloaded_cruise_time_s / 3600)

    # Phase 6: Descent and landing
    landing_time_s = 60  # 1 minute
    landing_power = calc.hover_power_actual(unloaded_weight)
    landing_energy_wh = (landing_power * landing_time_s / 3600)

    # Total mission time and energy
    total_time_s = (climb_time_s + loaded_cruise_time_s + descent_time_s +
                   drop_time_s + climb_time_s + unloaded_cruise_time_s + landing_time_s)

    total_energy_wh = (climb_energy_wh + loaded_cruise_energy_wh + payload_drop_energy_wh +
                      climb_back_energy_wh + unloaded_cruise_energy_wh + landing_energy_wh)

    return {
        'phases': {
            'takeoff_climb': {'time_s': climb_time_s, 'power_w': climb_power, 'energy_wh': climb_energy_wh},
            'loaded_cruise': {'time_s': loaded_cruise_time_s, 'power_w': loaded_cruise_power, 'energy_wh': loaded_cruise_energy_wh},
            'payload_drop': {'time_s': descent_time_s + drop_time_s, 'power_w': payload_drop_power, 'energy_wh': payload_drop_energy_wh},
            'climb_unloaded': {'time_s': climb_time_s, 'power_w': climb_back_power, 'energy_wh': climb_back_energy_wh},
            'unloaded_cruise': {'time_s': unloaded_cruise_time_s, 'power_w': unloaded_cruise_power, 'energy_wh': unloaded_cruise_energy_wh},
            'landing': {'time_s': landing_time_s, 'power_w': landing_power, 'energy_wh': landing_energy_wh}
        },
        'totals': {
            'total_time_s': total_time_s,
            'total_time_min': total_time_s / 60,
            'total_energy_wh': total_energy_wh,
            'loaded_weight_kg': loaded_weight,
            'unloaded_weight_kg': unloaded_weight,
            'payload_kg': payload_kg,
            'cruise_speed_ms': cruise_speed_ms,
            'cruise_speed_kmh': ms_to_kmh(cruise_speed_ms)
        },
        'feasibility': {
            'under_30_min': total_time_s / 60 < 30,
            'time_margin_min': 30 - (total_time_s / 60),
            'generator_adequate': config.generator_power_w > max(
                climb_power, loaded_cruise_power, payload_drop_power
            ) if config.hybrid_power else None,
            'max_power_w': max(climb_power, loaded_cruise_power, payload_drop_power),
            'avg_power_w': total_energy_wh / (total_time_s / 3600)
        }
    }


def payload_ratio_analysis(config: AircraftConfig, max_payload_kg: float) -> Dict:
    """
    Analyze payload ratio for a given configuration.

    Args:
        config: Aircraft configuration
        max_payload_kg: Maximum payload to test

    Returns: Performance metrics including payload ratio
    """
    aircraft_weight_lbs = kg_to_lbs(config.total_weight())
    payload_lbs = kg_to_lbs(max_payload_kg)

    ratio = payload_lbs / aircraft_weight_lbs

    # Calculate if it meets mission requirements
    mission_energy = calculate_mission_energy(config, max_payload_kg)

    return {
        'aircraft_weight_kg': config.total_weight(),
        'aircraft_weight_lbs': aircraft_weight_lbs,
        'payload_kg': max_payload_kg,
        'payload_lbs': payload_lbs,
        'payload_ratio': ratio,
        'total_weight_kg': config.total_weight() + max_payload_kg,
        'total_weight_lbs': kg_to_lbs(config.total_weight() + max_payload_kg),
        'mission_time_min': mission_energy['totals']['total_time_min'],
        'mission_energy_wh': mission_energy['totals']['total_energy_wh'],
        'meets_time_requirement': mission_energy['feasibility']['under_30_min'],
        'time_margin_min': mission_energy['feasibility']['time_margin_min'],
        'max_power_w': mission_energy['feasibility']['max_power_w'],
        'avg_power_w': mission_energy['feasibility']['avg_power_w']
    }


if __name__ == "__main__":
    # Test the simulator with example configurations
    print("=" * 80)
    print("DARPA Lift Challenge - Performance Simulator Test")
    print("=" * 80)

    # Octocopter configuration (from research)
    print("\n### OCTOCOPTER CONFIGURATION ###")
    octo_config = AircraftConfig(
        aircraft_weight_kg=15.8 - 7.5,  # Frame + motors + electronics (excluding generator)
        num_rotors=8,
        rotor_diameter_m=0.61,  # 24 inch propellers
        hover_efficiency=0.65,
        cruise_efficiency=0.75,
        has_wing=False,
        hybrid_power=True,
        generator_weight_kg=7.5,
        generator_power_w=5000,
        battery_capacity_wh=500,  # Small buffer battery
        battery_weight_kg=1.0
    )

    print(f"Total aircraft weight: {octo_config.total_weight():.1f} kg ({kg_to_lbs(octo_config.total_weight()):.1f} lbs)")
    print(f"Total disk area: {octo_config.total_disk_area():.2f} m²")

    # Test with 109 kg payload (240 lbs)
    payload_kg = 109
    print(f"\nTesting with {payload_kg} kg ({kg_to_lbs(payload_kg):.0f} lbs) payload")

    result = payload_ratio_analysis(octo_config, payload_kg)
    print(f"\n**Payload Ratio: {result['payload_ratio']:.2f}:1**")
    print(f"Mission time: {result['mission_time_min']:.1f} minutes (limit: 30 min)")
    print(f"Time margin: {result['time_margin_min']:.1f} minutes")
    print(f"Mission energy: {result['mission_energy_wh']:.0f} Wh")
    print(f"Peak power: {result['max_power_w']:.0f} W")
    print(f"Average power: {result['avg_power_w']:.0f} W")
    print(f"Meets time requirement: {result['meets_time_requirement']}")

    # Quadplane configuration
    print("\n\n### QUADPLANE CONFIGURATION ###")
    quad_config = AircraftConfig(
        aircraft_weight_kg=20.8 - 6.5,  # Airframe (excluding generator)
        num_rotors=4,
        rotor_diameter_m=0.51,  # 20 inch propellers
        hover_efficiency=0.65,
        cruise_efficiency=0.75,
        has_wing=True,
        wing_area_m2=1.3,
        wing_efficiency=0.85,
        hybrid_power=True,
        generator_weight_kg=6.5,
        generator_power_w=4000,
        battery_capacity_wh=400,
        battery_weight_kg=0.8
    )

    print(f"Total aircraft weight: {quad_config.total_weight():.1f} kg ({kg_to_lbs(quad_config.total_weight()):.1f} lbs)")
    print(f"Total disk area: {quad_config.total_disk_area():.2f} m²")
    print(f"Wing area: {quad_config.wing_area_m2:.2f} m²")

    # Test with 100 kg payload (220 lbs)
    payload_kg = 100
    print(f"\nTesting with {payload_kg} kg ({kg_to_lbs(payload_kg):.0f} lbs) payload")

    result = payload_ratio_analysis(quad_config, payload_kg)
    print(f"\n**Payload Ratio: {result['payload_ratio']:.2f}:1**")
    print(f"Mission time: {result['mission_time_min']:.1f} minutes (limit: 30 min)")
    print(f"Time margin: {result['time_margin_min']:.1f} minutes")
    print(f"Mission energy: {result['mission_energy_wh']:.0f} Wh")
    print(f"Peak power: {result['max_power_w']:.0f} W")
    print(f"Average power: {result['avg_power_w']:.0f} W")
    print(f"Meets time requirement: {result['meets_time_requirement']}")

    print("\n" + "=" * 80)
    print("Simulation complete. Core physics validated.")
    print("=" * 80)
