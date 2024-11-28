# Sets and Indices
- N = set of expedition members (i = 1,...,N) where N = 5
- M = set of river arms (j = 1,...,M) where M = 3
- T = set of time periods (t = 0,...,T_max)

# Parameters
- p[i,j] = processing time for member i to cross arm j
- K = large positive number (big-M)
- V = subset of N representing vehicles (all except pedestrians)

# Decision Variables
- x[i,j,t] = {1 if member i starts crossing arm j at time t; 0 otherwise}
- C = makespan (completion time)

# Objective Function
```
Minimize C
```

# Constraints

1. Each member must cross each arm exactly once:
```
∑(t∈T) x[i,j,t] = 1    ∀i∈{1,...,N}, ∀j∈{1,...,M}
```

2. No two vehicles can cross the same arm simultaneously:
```
∑(i∈V) ∑(t'=t to t+p[i,j]) x[i,j,t'] ≤ 1    ∀j∈{1,...,M}, ∀t∈T
```

3. Pedestrians cannot cross with vehicles on the same arm:
```
x[1,j,t] + ∑(i∈V) ∑(t'=t to t+p[i,j]) x[i,j,t'] ≤ 1    ∀j∈{1,...,M}, ∀t∈T
```
where member i=1 represents pedestrians

4. Sequential arm crossing (can't start next arm before finishing current):
```
∑(t∈T) (t + p[i,j])x[i,j,t] ≤ ∑(t∈T) t·x[i,j+1,t]    
∀i∈{1,...,N}, ∀j∈{1,...,M-1}
```

5. Completion time definition:
```
∑(t∈T) (t + p[i,M])x[i,M,t] ≤ C    ∀i∈{1,...,N}
```

6. Non-negativity and binary constraints:
```
C ≥ 0
x[i,j,t] ∈ {0,1}    ∀i∈{1,...,N}, ∀j∈{1,...,M}, ∀t∈T
```

# Model Properties
- Number of binary variables: N × M × |T|
- Number of continuous variables: 1 (C)
- The time index t creates a large number of variables and constraints
- Model size heavily depends on the chosen time horizon T_max
