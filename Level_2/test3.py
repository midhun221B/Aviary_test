#Aviary test script for a single-aisle transport aircraft optimization problem using the FwFm benchmark aircraft definition.
#-- IGNORE ---

#Import Aviary API
import aviary.api as av # type: ignore

#Phase_info
phase_info = {
    'pre_mission': {
        'include_takeoff': False,
        'optimize_mass': False,
    },
    'cruise': {
        'subsystem_options': {'aerodynamics': {'method': 'computed'}},
        'user_options': {
            'num_segments': 2,
            'order': 3,
            'mach_optimize': False,
            'mach_polynomial_order': 1,
            'mach_initial': (0.72, 'unitless'),
            'mach_final': (0.72, 'unitless'),
            'mach_bounds': ((0.7, 0.74), 'unitless'),
            'altitude_optimize': False,
            'altitude_polynomial_order': 1,
            'altitude_initial': (35000.0, 'ft'),
            'altitude_final': (35000.0, 'ft'),
            'altitude_bounds': ((23000.0, 38000.0), 'ft'),
            'throttle_enforcement': 'boundary_constraint',
            'time_initial_bounds': ((0.0, 0.0), 'min'),
            'time_duration_bounds': ((10.0, 30.0), 'min'),
        },
        'initial_guesses': {'time': ([0, 30], 'min')},
    },
    'post_mission': {
        'include_landing': False,
    },
}

# inputs that run_aviary() requires
aircraft_data = 'validation_cases/validation_data/test_models/aircraft_for_bench_FwFm.csv'
mission_method = 'energy_state'
mass_method = 'FLOPS'
optimizer = 'SLSQP'
objective_type = None
restart_filename = None

# Build problem
prob = av.AviaryProblem()

# Load aircraft and options data from user
# Allow for user overrides here
prob.load_inputs(aircraft_data, phase_info)

prob.check_and_preprocess_inputs()

prob.build_model()

prob.add_driver(optimizer, max_iter=0)

prob.add_design_variables()

# Load optimization problem formulation
# Detail which variables the optimizer can control
prob.add_objective(objective_type=objective_type)

prob.setup()

prob.run_aviary_problem()

print('done')