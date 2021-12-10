import numpy as np
import pulp

# Constraints
m = pulp.LpVariable('m', lowBound=0, upBound=None)
