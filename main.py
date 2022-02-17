import numpy as np
import pulp

# Parameters
D = ("Mon", "Tue", "Wed")
T = ("Morning", "Afternoon")
G = ("A", "B")
S = ("Math", "Lang")
I = ("Alejandro", "Alvaro")

m = np.zeros(len(D)*len(T)*len(G)*len(S))
y = np.zeros(len(I)*len(G)*len(S))

v_m = np.random.rand(len(D)*len(T)*len(G)*len(S))
v_y = np.random.rand(len(I)*len(G)*len(S))

# Constraints
m = pulp.LpVariable('m', lowBound=0, upBound=None)