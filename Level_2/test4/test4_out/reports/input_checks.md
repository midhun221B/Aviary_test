# Unspecified Hierarchy Variables
These aviary inputs are unspecified in aviary_inputs, and may be using default values defined in the Aviary metadata.

| Name | Value | Units | Description | Absolute Paths
| :- |  :- |  :- | :- | :- |
| **aircraft:battery:mass** | [0.] | lbm | total mass of the battery | ['pre_mission.core_subsystems.mass.mass_summation.propulsion_mass.aircraft:battery:mass']|
| **aircraft:canard:mass_scaler** | [1.] | unitless | mass scaler for canard structure | ['pre_mission.core_subsystems.mass.canard.aircraft:canard:mass_scaler']|
| **aircraft:canard:taper_ratio** | [0.] | unitless | canard theoretical taper ratio | ['pre_mission.core_subsystems.mass.canard.aircraft:canard:taper_ratio']|
| **aircraft:canard:wetted_area_scaler** | [1.] | unitless | canard wetted area scaler | ['pre_mission.core_subsystems.geometry.wetted_area.canard_swet.aircraft:canard:wetted_area_scaler']|
| **aircraft:design:external_subsystems_mass** | [0.] | lbm | Total mass of all user-defined external subsystems. These are bookkept as part of empty mass. | ['pre_mission.core_subsystems.mass.mass_summation.empty_mass_group.empty_mass.aircraft:design:external_subsystems_mass']|
| **aircraft:fuel:density** | [6.7] | lbm/galUS | fuel density (jet fuel typical density of 6.7 lbm/galUS used in the calculation of wing_capacity(if wing_capacity is not input) and in the calculation of fuel system weight. | ['pre_mission.core_subsystems.mass.fuel_capacity_group.wing_fuel_capacity.aircraft:fuel:density', 'pre_mission.core_subsystems.mass.unusable_fuel.aircraft:fuel:density']|
| **aircraft:fuel:wing_fuel_fraction** | [0.] | unitless | fraction of total theoretical wing volume used for wing fuel | ['pre_mission.core_subsystems.mass.fuel_capacity_group.wing_fuel_capacity.aircraft:fuel:wing_fuel_fraction']|
| **aircraft:fuel:wing_ref_capacity** | [0.] | lbm | reference fuel volume | ['pre_mission.core_subsystems.mass.fuel_capacity_group.wing_fuel_capacity.aircraft:fuel:wing_ref_capacity']|
| **aircraft:fuel:wing_ref_capacity_area** | [0.] | unitless | reference wing area for fuel capacity | ['pre_mission.core_subsystems.mass.fuel_capacity_group.wing_fuel_capacity.aircraft:fuel:wing_ref_capacity_area']|
| **aircraft:fuel:wing_ref_capacity_term_a** | [0.] | unitless | scaling factor A | ['pre_mission.core_subsystems.mass.fuel_capacity_group.wing_fuel_capacity.aircraft:fuel:wing_ref_capacity_term_a']|
| **aircraft:fuel:wing_ref_capacity_term_b** | [0.] | unitless | scaling factor B | ['pre_mission.core_subsystems.mass.fuel_capacity_group.wing_fuel_capacity.aircraft:fuel:wing_ref_capacity_term_b']|
| **aircraft:fuselage:laminar_flow_lower** | [0.] | unitless | define percent laminar flow for fuselage lower surface | ['traj.param_comp.parameters:aircraft:fuselage:laminar_flow_lower']|
| **aircraft:fuselage:laminar_flow_upper** | [0.] | unitless | define percent laminar flow for fuselage upper surface | ['traj.param_comp.parameters:aircraft:fuselage:laminar_flow_upper']|
| **aircraft:horizontal_tail:laminar_flow_lower** | [0.] | unitless | define percent laminar flow for horizontal tail lower surface | ['traj.param_comp.parameters:aircraft:horizontal_tail:laminar_flow_lower']|
| **aircraft:horizontal_tail:laminar_flow_upper** | [0.] | unitless | define percent laminar flow for horizontal tail upper surface | ['traj.param_comp.parameters:aircraft:horizontal_tail:laminar_flow_upper']|
| **aircraft:nacelle:laminar_flow_lower** | [0.] | unitless | define percent laminar flow for nacelle lower surface for each engine model | ['traj.param_comp.parameters:aircraft:nacelle:laminar_flow_lower']|
| **aircraft:nacelle:laminar_flow_upper** | [0.] | unitless | define percent laminar flow for nacelle upper surface for each engine model | ['traj.param_comp.parameters:aircraft:nacelle:laminar_flow_upper']|
| **aircraft:vertical_tail:laminar_flow_lower** | [0.] | unitless | define percent laminar flow for vertical tail lower surface | ['traj.param_comp.parameters:aircraft:vertical_tail:laminar_flow_lower']|
| **aircraft:vertical_tail:laminar_flow_upper** | [0.] | unitless | define percent laminar flow for vertical tail upper surface | ['traj.param_comp.parameters:aircraft:vertical_tail:laminar_flow_upper']|
| **aircraft:wing:aspect_ratio_reference** | [0.] | unitless | Reference aspect ratio, used for detailed wing mass estimation. | ['pre_mission.core_subsystems.mass.wing_group.wing_bending_material_factor.aircraft:wing:aspect_ratio_reference']|
| **aircraft:wing:bwb_aftbody_mass** | [0.] | lbm | wing mass breakdown term 4 | ['pre_mission.core_subsystems.mass.wing_group.wing_total.aircraft:wing:bwb_aftbody_mass']|
| **aircraft:wing:dihedral** | [0.] | deg | wing dihedral (positive) or anhedral (negative) angle | ['pre_mission.core_subsystems.geometry.main_landing_gear_length.aircraft:wing:dihedral']|
| **aircraft:wing:laminar_flow_lower** | [0.] | unitless | define percent laminar flow for wing lower surface | ['traj.param_comp.parameters:aircraft:wing:laminar_flow_lower']|
| **aircraft:wing:laminar_flow_upper** | [0.] | unitless | define percent laminar flow for wing upper surface | ['traj.param_comp.parameters:aircraft:wing:laminar_flow_upper']|
| **aircraft:wing:span_efficiency_factor** | [1.] | unitless | coefficient for calculating span efficiency for extreme taper ratios | ['traj.param_comp.parameters:aircraft:wing:span_efficiency_factor']|
| **aircraft:wing:thickness_to_chord_reference** | [0.] | unitless | Reference thickness-to-chord ratio, used for detailed wing mass estimation. | ['pre_mission.core_subsystems.mass.wing_group.wing_bending_material_factor.aircraft:wing:thickness_to_chord_reference']|
| **mission:reserve_fuel** | [0.] | lbm | fuel burned during reserve phases, this does not include fuel burned in regular phases | ['post_mission.reserve_fuel.reserve_fuel_burned']|
| **mission:takeoff:ascent_duration** | [0.] | s | duration of the ascent phase of takeoff | ['fuel_obj.ascent_duration', 'range_obj.ascent_duration']|
| **mission:taxi:fuel_taxi_in** | [0.] | lbm | Fuel burned to taxi from the runway to the gate. Can be used with energy-stand and 2DOF EOM. | ['post_mission.block_fuel_comp.fuel_burned_taxi_in']|
| **mission:taxi:fuel_taxi_out** | [0.] | lbm | Fuel burned to taxi from the gate to the runway. Only used in energy-state EOM. Not used in 2DOF EOM. | ['takeoff_mass_comp.taxi_out_fuel_burn']|

# Unspecified Local Variables
These local subsystem inputs are unconnected, and may be using default values specified in the component.

| Name | Value | Units | Absolute Paths
| :- |  :- |  :- | :- |
| **pre_mission.wing_characteristic_lengths.prep_geom:_Names:CROOT** | [0.] | unitless | ['pre_mission.core_subsystems.geometry.wing_characteristic_lengths.prep_geom:_Names:CROOT']|
| **reserve_fuel_margin_mass** | [0.] | lbm | ['post_mission.reserve_fuel.reserve_fuel_margin_mass']|
| **target_range** | [1915.] | nmi | ['range_constraint.target_range']|
| **traj.climb_1.rhs_all.vectorize_performance.electric_power_in_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | kW | ['traj.phases.climb_1.rhs_all.solver_sub.propulsion.vectorize_performance.electric_power_in_0']|
| **traj.climb_1.rhs_all.vectorize_performance.propeller_tip_speed_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | ft/s | ['traj.phases.climb_1.rhs_all.solver_sub.propulsion.vectorize_performance.propeller_tip_speed_0']|
| **traj.climb_1.rhs_all.vectorize_performance.rotations_per_minute_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | rpm | ['traj.phases.climb_1.rhs_all.solver_sub.propulsion.vectorize_performance.rotations_per_minute_0']|
| **traj.climb_1.rhs_all.vectorize_performance.shaft_power_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | hp | ['traj.phases.climb_1.rhs_all.solver_sub.propulsion.vectorize_performance.shaft_power_0']|
| **traj.climb_1.rhs_all.vectorize_performance.shaft_power_max_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | hp | ['traj.phases.climb_1.rhs_all.solver_sub.propulsion.vectorize_performance.shaft_power_max_0']|
| **traj.climb_1.rhs_all.vectorize_performance.t4_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | degR | ['traj.phases.climb_1.rhs_all.solver_sub.propulsion.vectorize_performance.t4_0']|
| **traj.cruise.rhs_all.vectorize_performance.electric_power_in_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | kW | ['traj.phases.cruise.rhs_all.solver_sub.propulsion.vectorize_performance.electric_power_in_0']|
| **traj.cruise.rhs_all.vectorize_performance.propeller_tip_speed_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | ft/s | ['traj.phases.cruise.rhs_all.solver_sub.propulsion.vectorize_performance.propeller_tip_speed_0']|
| **traj.cruise.rhs_all.vectorize_performance.rotations_per_minute_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | rpm | ['traj.phases.cruise.rhs_all.solver_sub.propulsion.vectorize_performance.rotations_per_minute_0']|
| **traj.cruise.rhs_all.vectorize_performance.shaft_power_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | hp | ['traj.phases.cruise.rhs_all.solver_sub.propulsion.vectorize_performance.shaft_power_0']|
| **traj.cruise.rhs_all.vectorize_performance.shaft_power_max_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | hp | ['traj.phases.cruise.rhs_all.solver_sub.propulsion.vectorize_performance.shaft_power_max_0']|
| **traj.cruise.rhs_all.vectorize_performance.t4_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | degR | ['traj.phases.cruise.rhs_all.solver_sub.propulsion.vectorize_performance.t4_0']|
| **traj.descent_1.rhs_all.vectorize_performance.electric_power_in_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | kW | ['traj.phases.descent_1.rhs_all.solver_sub.propulsion.vectorize_performance.electric_power_in_0']|
| **traj.descent_1.rhs_all.vectorize_performance.propeller_tip_speed_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | ft/s | ['traj.phases.descent_1.rhs_all.solver_sub.propulsion.vectorize_performance.propeller_tip_speed_0']|
| **traj.descent_1.rhs_all.vectorize_performance.rotations_per_minute_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | rpm | ['traj.phases.descent_1.rhs_all.solver_sub.propulsion.vectorize_performance.rotations_per_minute_0']|
| **traj.descent_1.rhs_all.vectorize_performance.shaft_power_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | hp | ['traj.phases.descent_1.rhs_all.solver_sub.propulsion.vectorize_performance.shaft_power_0']|
| **traj.descent_1.rhs_all.vectorize_performance.shaft_power_max_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | hp | ['traj.phases.descent_1.rhs_all.solver_sub.propulsion.vectorize_performance.shaft_power_max_0']|
| **traj.descent_1.rhs_all.vectorize_performance.t4_0** | [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] | degR | ['traj.phases.descent_1.rhs_all.solver_sub.propulsion.vectorize_performance.t4_0']|


