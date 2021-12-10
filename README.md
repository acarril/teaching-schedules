# Teaching Schedules

## Install

You need Python 3.9.9 to run the code in this project, which is defined in [.python-version](.python-version).
Dependencies are specified in [requirements.txt](requirements.txt).

More detailed instructions on how to set up Python in macOS can be found [here](https://gist.github.com/acarril/a415b068bd89ebb256d82f962f7f3272).

## Optimization library: PuLP

We model the school timetable problem using [PuLP](https://github.com/coin-or/pulp), a popular linear programming modeler for Python. 
### Example

We adapt a simple example from the [PuLP documentation](https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html) (the "blending problem"), which is solved in [blending_problem.py](tests/blending_problem.py).