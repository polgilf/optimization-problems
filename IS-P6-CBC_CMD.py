from pulp import *
import pandas as pd

solver = 'PULP_CBC_CMD'
report_file_name = 'results_'+solver+'.txt'
output_file_name = 'output_'+solver+'.log'

proces_time = {'A1':{'TTC':6,'TTL':2,'C':6,'P': 4,'MM':5},
               'A2':{'TTC':10,'TTL':8,'C':4,'P':2,'MM':3},
               'A3':{'TTC':4,'TTL':3,'C':5,'P':7,'MM':4}}

# 
M = len(proces_time.keys()) # M = 3
N = len(proces_time['A1'].keys()) # N = 5

machine_names = [key for key in proces_time.keys()] # ['A1', 'A2', 'A3']
job_names = [key for key in proces_time['A1'].keys()] # ['TTC', 'TTL', 'C', 'P', 'MM']

# Ranges where indexes are defined
jobs = range(1,N+1)
machines = range(1,M+1)

# convert data to dictionary {(i,k): value}   (i=machine, j=job)
p = {(i,j): proces_time[machine_names[i-1]][job_names[j-1]] for j in jobs for i in machines}

# Create the model
prob = LpProblem("flowshop-is-p6", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((j,k) for j in range(N+1) for k in range(N+1)), cat='Binary')
s = LpVariable.dicts("s", ((k,i) for k in range(N+1) for i in range(M+1)), lowBound=0)

# Constraints
# One job is scheduled only once
for k in jobs: 
    prob += lpSum(x[(j,k)] for j in jobs) == 1

# Each possible order is used only once
for j in jobs: 
    prob += lpSum(x[(j,k)] for k in jobs) == 1

# Initial conditions
for i in machines:
    prob += s[0,i] == 0  # Dummy job 0 finishes at time 0

for k in jobs:
    prob += s[k,0] == 0  # Dummy machine 0 has zero processing time

# Machine timing constraints (take into acount the maximum betwen the previous machine of the same job and the next machine of the previous job)
for i in range(1, M+1):
    for k in jobs:
        prob += s[k,i] >= s[k,i-1] + lpSum(x[(j,k)] * p[(i,j)] for j in jobs)
        prob += s[k,i] >= s[k-1,i] + lpSum(x[(j,k)] * p[(i,j)] for j in jobs)

# Objective: Minimize makespan
prob += s[N,M]

# Solve the problem
# Not detailed output but essential information
# Store output in a variable (string) to print it later
prob.solve(PULP_CBC_CMD(msg=True, logPath = output_file_name))

# Fom log file, take only the sub string from 'Result - Optimal solution found' to the end of the file
with open(output_file_name, 'r') as f:
    log = str(f.read())
    log = log[log.find('Result - Optimal solution found'):]

# Store solution in a dictionary sch_dict = {(job, machine): start_time} and order_dict = {order: job} = {1: jobname, 2: jobname, ...}
sch_dict = {}
order_dict = {}
x_names_ranges = {v: k for k, v in x.items()}
s_names_ranges = {v: k for k, v in s.items()}

for v in prob.variables():
    if v.varValue > 0:
        value = v.varValue
        if v.name[0] == 'x':
            (i, k) = x_names_ranges[v]
            order_dict[k] = i
        elif v.name[0] == 's':
            (k, j) = s_names_ranges[v]
            sch_dict[(k, j)] = value
order_dict = dict(sorted(order_dict.items()))

# Decode the results to match original names
results_order = {k: job_names[v-1] for k, v in order_dict.items()}
results_endtime = {(k, machine_names[j-1]): v for (k, j), v in sch_dict.items()}

# New dictionary (order, machinename, jobname) : end_time_value, sorted by order and then by machine
results_detailed = {}
for (k, j), v in sch_dict.items():
    results_detailed[(k, machine_names[j-1], results_order[k])] = v

# results_order to dataframe
df_order = pd.DataFrame.from_dict(results_order, orient='index', columns=['jobname'])
# results_detail to dataframe
df_detailed = pd.DataFrame.from_dict(results_detailed, orient='index', columns=['end_time'])

report = {
    'name': prob.name,
    'solver': prob.solver.name,
    'objective': prob.objective,
    'num_variables': len(prob.variables()),
    'num_constraints': len(prob.constraints),
    'solutionTime': prob.solutionTime,
    'solutionCpuTime': prob.solutionCpuTime,
    'status': prob.status,
    'sol_status': prob.sol_status,
    'noOverlap': prob.noOverlap,
    #'variables': prob.variables(),
    #'constraints': prob.constraints    
}

# SAVE SAME PRINTED INFO TO FILE report_file_name

with open(report_file_name, 'w') as f:
    f.write('\n#################################\n')
    f.write('###-------- Results --------###')
    f.write('\n#################################\n')
    f.write('\n#----------------------------------#\n')
    f.write('Name: '+report['name']+'\n')
    f.write('Solver: '+report['solver']+'\n')
    f.write('\n#----------------------------------#\n')
    f.write('REPORT:\n')
    for key, values in report.items():
        f.write(key+': '+str(values)+'\n')
    f.write('\n#----------------------------------#\n')
    f.write('RESULTS:\n')
    f.write('\n#----------------------------------#\n')
    f.write('Order:\n')
    f.write(df_order.to_string())
    f.write('\n#----------------------------------#\n')
    f.write('Schedule:\n')
    f.write(df_detailed.to_string())
    f.write('\n#----------------------------------#\n')
    f.write('Log:\n')
    f.write(log)
    f.write('\n#----------------------------------#\n')
    f.close()

