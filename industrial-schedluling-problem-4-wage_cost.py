from docplex.mp.model import Model

# To print log_output to a file instead of the console
import os
import sys
from contextlib import contextmanager

# Path and file names:
project_dir = os.getcwd()
output_file_name = 'wage-costs-100-output-cn0.txt'

# Create the model
mdl = Model('workforce scheduling')

# DATA
T = 6 # Number of bimesters
D = [5200, 3600, 6500, 5400, 8100, 7000] # Demand on each bimester [units]
deltaW = 20 # Allowed variation of workforce each bimester [workers]
cH = 50 # Hiring cost [m.u./worker]
cF = 70 # Firing cost [m.u./worker]
#cO = 25 # Differential Overtime production cost [m.u./unit]
cs = 15 # Storage cost [m.u./unit·bimester]
S0 = 700 # Initial storage [units]
SF = 700 # Final storage [units]
W0 = 150 # Initial workforce [workers]
CN = 40 # Production capacity normal hours [units/worker·bimester]
CE = 12 # Production capacity overtime hours [units/worker·bimester]

cW = 100 # Wage cost [m.u./worker]
cN = 0 # Production cost normal hours [m.u./unit]
cE = cN + 25 # Production cost overtime hours [m.u./unit]

# VARIABLES

W = mdl.integer_var_dict(range(0,T+1), name='W', lb=0) # Workforce at the beginning of bimiester [workers]
WH = mdl.integer_var_dict(range(1,T+1), name='WH', lb=0) # Workforce hired at the beginning of bimester [workers]
WF = mdl.integer_var_dict(range(1,T+1), name='WF', lb=0) # Workforce fired at the beginning of bimester [workers]
PN = mdl.integer_var_dict(range(1,T+1), name='PN', lb=0) # Production normal hours at bimester [units]
PE = mdl.integer_var_dict(range(1,T+1), name='PE', lb=0) # Production overtime hours at bimester [units]
S = mdl.integer_var_dict(range(0,T+1), name='S', lb=0) # Storage at the end of bimester [units]
TC = mdl.continuous_var(name='TC', lb=0) # Total cost [m.u.]

# CONSTRAINTS

# Initial conditions
mdl.add_constraint(W[0] == W0, ctname='Initial workforce')
mdl.add_constraint(S[0] == S0, ctname='Initial storage')
mdl.add_constraint(S[T] == SF, ctname='Final storage')

# Workforce balance
mdl.add_constraints(W[t] == W[t-1] + WH[t] - WF[t] for t in range(1,T+1))

# Material balance
mdl.add_constraints(S[t] == S[t-1] + PN[t] + PE[t] - D[t-1] for t in range(1,T+1))

# Production capacity
mdl.add_constraints(PN[t] == CN * W[t] for t in range(1,T+1))
mdl.add_constraints(PE[t] <= CE * W[t] for t in range(1,T+1))

# Hiring and firing
mdl.add_constraints(WH[t] <= deltaW for t in range(1,T+1))
mdl.add_constraints(WF[t] <= deltaW for t in range(1,T+1))

# Total cost
mdl.add_constraint(TC == mdl.sum(cW*W[t] + cH*WH[t] + cF*WF[t] + cE*PE[t] + cN*PN[t] + cs*S[t] for t in range(1,T+1)))

# Objective function
mdl.minimize(TC)

# SOLVE
# Print log_output to .txt file
# Custom context manager to redirect stdout
@contextmanager
def redirect_stdout_to_file(file_path):
    original_stdout = sys.stdout
    with open(file_path, 'w') as f:
        sys.stdout = f
        yield
        sys.stdout = original_stdout

file_path = os.path.join(project_dir, output_file_name)

print('Starting execution')

with redirect_stdout_to_file(file_path):
    solution = mdl.solve(url=None, log_output=True)
    print("\n*** SOLVE STATUS ***\n")
    print(mdl.solve_details.status)
    print("\n*** REPORT ***\n")
    print(mdl.report())
    print("\n*** RESULTS ***\n")

    # Print results
    # Total cost
    print('Total cost:', mdl.solution.get_value(TC))
    # Worforce at the beginning of each bimester
    print('Workforce at the beginning of each bimester:')
    for t in range(1,T+1):
        print(f'W[{t}] = {mdl.solution.get_value(W[t])}')
    # Workforce hired at the beginning of each bimester
    print('Workforce hired at the beginning of each bimester:')
    for t in range(1,T+1):
        print(f'WH[{t}] = {mdl.solution.get_value(WH[t])}')
    # Workforce fired at the beginning of each bimester
    print('Workforce fired at the beginning of each bimester:')
    for t in range(1,T+1):
        print(f'WF[{t}] = {mdl.solution.get_value(WF[t])}')
    # Production normal hours at each bimester
    print('Production normal hours at each bimester:')
    for t in range(1,T+1):
        print(f'PN[{t}] = {mdl.solution.get_value(PN[t])}')
    # Production overtime hours at each bimester
    print('Production overtime hours at each bimester:')
    for t in range(1,T+1):
        print(f'PE[{t}] = {mdl.solution.get_value(PE[t])}')