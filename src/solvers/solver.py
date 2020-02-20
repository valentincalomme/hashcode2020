from __future__ import annotations


class Solver:
    """"""

    def __call__(self, problem: Problem) -> Solution:

        solution = self.solve(problem)

        if not solution.is_valid():

            raise Exception("Solution is invalid!")

        return solution

    def yield_solutions(self, problem: Problem) -> Solution:

        raise NotImplementedError
