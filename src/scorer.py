from __future__ import annotations


class Scorer:
    """Implements the scoring system"""

    def score(self, problem: Problem, solution: Solution) -> int:
        """Scores a solution given a problem

        Parameters
        ----------
        problem : Problem
            Problem to solve
        solution : Solution
            Solution to the problem

        Returns
        -------
        int
            Score as a positive integer
        """

        raise NotImplementedError

    def is_valid(self, solution: Solution, problem: Problem) -> bool:
        """Checks whether the solution is valid

        Returns
        -------
        bool
            True if solution is valid, False if it isn't
        """

        raise NotImplementedError
