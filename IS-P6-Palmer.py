import pandas as pd
import numpy as np
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

# Computing bounds
# k1 = sum of all job's processing times in machine 1 + minimum of all job's processing times in machine 2+3
k1 = sum([p[1,j] for j in jobs]) + min([p[2,j] + p[3,j] for j in jobs])

# k2 = sum of all job's processing times in machine 2 + minimum of all possible combinations of job's processing times in machine 1+3 except sum for same job
k2 = sum([p[2,j] for j in jobs]) + min([p[1,j] + p[3,k] for j in jobs for k in jobs if k!=j])

# k3 = sum of all job's processing times in machine 3 + minimum of all job's processing times in machine 1+2
k3 = sum([p[3,j] for j in jobs]) + min([p[1,j] + p[2,j] for j in jobs])

K = max(k1,k2,k3)

print('k1:', k1, 'k2:', k2, 'k3:', k3, 'K:', K)

# Compute virtual machine processing times
S = {1: {j: sum([p[i,j]*(M-i) for i in machines]) for j in jobs},
     2: {j: sum([p[i,j]*(i-1) for i in machines]) for j in jobs}}
S[3] = {j: S[1][j] - S[2][j] for j in jobs}

S_df = pd.DataFrame(S).T

# Sorting jobs by increasing order of S_3,j
sorted_jobs = sorted(jobs, key=lambda j: S[3][j])


sorted_jobs_names = [job_names[j-1] for j in sorted_jobs]
# Print sorted jobs corresponding to jobnames

# Compute Cmax
C = {}
for i in machines:
    for k in jobs:
        j = sorted_jobs[k-1]
        if i == 1 and k == 1:
            C[i,k] = p[i,j]
        elif i > 1 and k == 1:
            C[i,k] = C[i-1,k] + p[i,j]
        elif i == 1 and k > 1:
            C[i,k] = C[i,k-1] + p[i,j]
        else:
            C[i,k] = max(C[i,k-1], C[i-1,k]) + p[i,j]

# C to dataframe {(1, 1): 6,  (1, 2): 8,  (1, 3): 14,... } where (i,j) = C[i,j] (i=machine, j=job)
C_df = pd.DataFrame(C.values(), index=pd.MultiIndex.from_tuples(C.keys())).unstack()
# Columns are sorted_jobs_names (in this order)
C_df.columns = sorted_jobs_names
C_max = max(C.values())

# Print
print('\nProcess time:')
print(proces_time_df)
print('\np[i,j]:')
print(p_df)
print('\nS:')
print(S_df)
print('\nC_max:', C_max)
print('\nSorted jobs:', sorted_jobs)
print('\nSorted job names:', sorted_jobs_names)

print('\nC:')
print(C_df)

# End time
execution_end_time = time.time()

# Execution time
execution_time = execution_end_time - execution_start_time
print(f"Execution time: {execution_time} seconds")

'''
Output:

k1: 30 k2: 33 k3: 29 K: 33

Process time:
    TTC  TTL  C  P  MM
A1    6    2  6  4   5
A2   10    8  4  2   3
A3    4    3  5  7   4

p[i,j]:
    0
    1  2  3  4  5
1   6  2  6  4  5
2  10  8  4  2  3
3   4  3  5  7  4

S:
    1   2   3   4   5
1  22  12  16  10  13
2  18  14  14  16  11
3   4  -2   2  -6   2

C_max: 37

Sorted jobs: [4, 2, 3, 5, 1]

Sorted job names: ['P', 'TTL', 'C', 'MM', 'TTC']

C:
    P  TTL   C  MM  TTC
1   4    6  12  17   23
2   6   14  18  21   33
3  13   17  23  27   37
Execution time: 0.023905038833618164 seconds
'''

