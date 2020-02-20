from __future__ import annotations


from solvers import Solver


class RandomSolver(Solver):
    def yield_solutions(self, problem: Problem) -> Solution:

        raise NotImplementedError
