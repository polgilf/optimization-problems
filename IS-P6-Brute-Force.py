import pandas as pd
import numpy as np
from itertools import permutations
import time

execution_start_time = time.time()

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

# convert data to dictionary {(i,j): value}   (i=machine, j=job)
p = {(i,j): proces_time[machine_names[i-1]][job_names[j-1]] for j in jobs for i in machines}

# Dataframes
proces_time_df = pd.DataFrame(proces_time).T
p_df = pd.DataFrame(p.values(), index=pd.MultiIndex.from_tuples(p.keys())).unstack()

# All possible orders of jobs
all_orders = list(permutations(jobs))
print('Number of all possible orders:', len(all_orders))

all_Cmax = {}
for order in all_orders:
    C = {}
    # Compute Cmax
    for i in machines:
        for k in jobs:
            j = order[k-1]
            if i == 1 and k == 1:
                C[i,k] = p[i,j]
            elif i > 1 and k == 1:
                C[i,k] = C[i-1,k] + p[i,j]
            elif i == 1 and k > 1:
                C[i,k] = C[i,k-1] + p[i,j]
            else:
                C[i,k] = max(C[i,k-1], C[i-1,k]) + p[i,j]
    C_max = max(C.values())
    all_Cmax[order] = C_max

# Find the best order (lowest value in all_Cmax)
best_order = min(all_Cmax, key=all_Cmax.get)
# best_order_names
best_order_names = [job_names[j-1] for j in best_order]

print(best_order_names, 'value:', all_Cmax[best_order])

# End time
execution_end_time = time.time()

# Execution time
execution_time = execution_end_time - execution_start_time
print(f"Execution time: {execution_time} seconds")

'''

Output:

Number of all possible orders: 120
['TTL', 'P', 'TTC', 'C', 'MM'] value: 35
Execution time: 0.0050008 seconds

'''