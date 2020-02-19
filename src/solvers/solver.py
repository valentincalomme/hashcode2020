from __future__ import annotations


class Solver:
    """"""

    def __call__(self, problem: Problem) -> Solution:

        solution = self.solve(problem)

        if not solution.is_valid():

            raise Exception("Solution is invalid!")

        return solution

    def solve(self, problem: Problem) -> Solution:

        raise NotImplementedError
