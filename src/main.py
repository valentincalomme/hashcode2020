import os

from problem import Problem

# from solvers.raw_potential_solver import RawPotentialSolver
# from solvers.random_solver import RandomSolver
from solvers.greedy_solver import GreedySolver

problems = {}

folder = "../data/problems"

for filename in os.listdir(folder):

    problems[filename[0]] = Problem(
        name=filename[0], filename=os.path.join(folder, filename)
    )

# solver = RandomSolver()
# solver = RawPotentialSolver()
solver = GreedySolver()

for name, problem in problems.items():

    for i, solution in enumerate(solver.yield_solutions(problem)):
        print(solution.to_file())
        break
