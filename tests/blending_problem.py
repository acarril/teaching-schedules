# Simple PuLP example; source: https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html
import pulp as p

# Create the 'prob' variable to contain the problem data
problem = p.LpProblem('WhiskasProblem', p.LpMinimize)

# The 2 variables Beef and Chicken are created with a lower limit of zero
x1 = p.LpVariable('ChickenPercent', 0, None, p.LpInteger)
x2 = p.LpVariable('BeefPercent', 0)

# The objective function is added to 'prob' first
problem += 0.013 * x1 + 0.008 * x2, "Total Cost of Ingredients per can"

# The five constraints are entered
problem += x1 + x2 == 100, "PercentagesSum"
problem += 0.100 * x1 + 0.200 * x2 >= 8.0, "ProteinRequirement"
problem += 0.080 * x1 + 0.100 * x2 >= 6.0, "FatRequirement"
problem += 0.001 * x1 + 0.005 * x2 <= 2.0, "FibreRequirement"
problem += 0.002 * x1 + 0.005 * x2 <= 0.4, "SaltRequirement"

# The problem is solved using PuLP's choice of Solver
problem.solve()

# Each of the variables is printed with it's resolved optimum value
for var in problem.variables():
    print(var.name, "=", var.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can =", p.value(problem.objective))
