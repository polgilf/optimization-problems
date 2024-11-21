from docplex.mp.model import Model

# Create the model
mdl = Model('revenue_optimization')

# Variables

p1 = mdl.continuous_var(name='p1', lb=0, ub=10000/8)
p2 = mdl.continuous_var(name='p2', lb=0, ub=16000/10)
q1 = mdl.continuous_var(name='q1', lb=0)
q2 = mdl.continuous_var(name='q2', lb=0)


# Define other variables
profit = mdl.continuous_var(name='profit')
income = mdl.continuous_var(name='income')
costs = mdl.continuous_var(name='costs')

# Quadratic functions
quadratic_function1 = mdl.continuous_var(name='quadratic_function1', lb=0)
quadratic_function2 = mdl.continuous_var(name='quadratic_function2', lb=0)

# Demand constraints
mdl.add_constraint(q1 == 10000 - 8*p1, 'demand1')
mdl.add_constraint(q2 == 16000 - 10*p2, 'demand2')

# Resource constraints
mdl.add_constraint(0.1*q1 + 0.2*q2 <= 600, 'machine_hours')
mdl.add_constraint(0.5*q1 + 0.3*q2 <= 3000, 'raw_material')


# Objective (quadratic terms are handled directly)
mdl.add_constraint(costs == 2000 * (0.1*q1 + 0.2*q2) + 500 * (0.5*q1 + 0.3*q2), 'costs')

#mdl.add_constraint(quadratic_function1 == p1**2, 'quadratic_function1')
#mdl.add_constraint(quadratic_function2 == p2**2, 'quadratic_function2')
mdl.add_constraint(quadratic_function1 >= p1**2, 'quadratic_function1')
mdl.add_constraint(quadratic_function2 >= p2**2, 'quadratic_function2')

mdl.add_constraint(income == 10000*p1 - 8 * quadratic_function1 + 16000*p2 - 10 * quadratic_function2, 'income')
mdl.add_constraint(profit == income - costs, 'profit')

mdl.minimize(-profit)
#mdl.maximize(profit)

mdl.parameters.optimalitytarget = 3  # Non-convex QCP

# Solve
solution = mdl.solve(log_output=True)

# Print results
if solution:
    print(f"Optimal p1: {solution.get_value(p1):.2f}")
    print(f"Optimal p2: {solution.get_value(p2):.2f}")
    print(f"Optimal q1: {solution.get_value(q1):.2f}")
    print(f"Optimal q2: {solution.get_value(q2):.2f}")
    print(f"Maximum profit: {-solution.objective_value:.2f}")