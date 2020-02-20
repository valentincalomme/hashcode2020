from __future__ import annotations

import numpy as np

from solution import Solution
from solvers import Solver


class GreedySolver(Solver):
    """Sorts libraries based on greedy criteria, then
    for each library, the books are sorted accordingly"""

    def yield_solutions(self, problem: Problem) -> Solution:

        # start with library with shortest sign up time
        libraries = sorted(problem.libraries, key=lambda x: x.sign_up_time)

        for library in libraries:

            library.books_to_scan = sorted(library.books, key=lambda x: x.book_score, reverse=True)

        solution = Solution(problem_name=problem.name, libraries=libraries)

        yield solution
