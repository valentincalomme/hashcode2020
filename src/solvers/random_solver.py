from __future__ import annotations

import numpy as np

from solution import Solution
from solvers import Solver


class RandomSolver(Solver):
    def yield_solutions(self, problem: Problem) -> Solution:

        while True:

            libraries = np.random.permutation(problem.libraries)

            for library in libraries:

                library.books_to_scan = np.random.permutation(library.books)

            solution = Solution(problem_name=problem.name, libraries=libraries)

            yield solution