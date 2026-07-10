#Example:2
#Aviary test script for a single-aisle transport aircraft optimization problem using the FwFm benchmark aircraft definition.
#-- IGNORE ---

# Import Aviary API
import aviary.api as av # type: ignore

# Phase_info
#import pre-built phase info dictionary
from aviary.models.missions.energy_state_default import phase_info # type: ignore

# Suppress outputs by setting verbosity as zero (quiet mode)
prob = av.AviaryProblem(verbosity=0)

# Load aircraft defination csv (Aviary's FwFm — "Flops with Flops mission" — benchmark validation aircraft, a single-aisle transport)
prob.load_inputs(
    'validation_cases/validation_data/test_models/aircraft_for_bench_FwFm.csv', phase_info
)

# Sanity check inputs and guess initial conditions for mission phases
prob.check_and_preprocess_inputs()

# Have Aviary build the OpenMDAO model with pre-mission, mission, and post-mission components
prob.build_model()

# Selecting optimizer and iteration limit are optional
prob.add_driver('SLSQP', max_iter=20)

# Add the default design variables needed to size the aircraft
prob.add_design_variables()

# Add wing area and engine scaling as additional design variables
prob.model.add_design_var(av.Aircraft.Engine.SCALE_FACTOR, lower=0.8, upper=1.2, ref=1)
prob.model.add_design_var(av.Aircraft.Wing.AREA, lower=1200, upper=1800, units='ft**2', ref=1400)

# Add the default objective function (default- minimum fuel burn)
prob.add_objective()

# Add constraints for wing loading and thrust-to-weight ratio
prob.model.add_constraint(av.Aircraft.Design.WING_LOADING, lower=120, units='lbf/ft**2')
prob.model.add_constraint(av.Aircraft.Design.THRUST_TO_WEIGHT_RATIO, lower=0.35)

# Standard OpenMDAO problem setup step
prob.setup()

# Run the optimization problem
prob.run_aviary_problem()

#prob.model.list_outputs(val=True, units=True)


#Results
print(f"\nTakeoff Gross Weight = {prob.get_val(av.Mission.Takeoff.FINAL_MASS, units='lbm')[0]} lbm")

print("\nDesign Variables")
print("---------------")
print(f"Engine Scale Factor (started at 1) = {prob.get_val(av.Aircraft.Engine.SCALE_FACTOR)[0]}")
print(f"Wing Area (started at 1370) = {prob.get_val(av.Aircraft.Wing.AREA, units='ft**2')[0]} ft^2")

print("\nConstraints")
print("-----------")
print(f"Wing Loading = {prob.get_val(av.Aircraft.Design.WING_LOADING, units='lbf/ft**2')[0]} lbf/ft^2")
print(f"Thrust/Weight Ratio = {prob.get_val(av.Aircraft.Design.THRUST_TO_WEIGHT_RATIO)[0]}")