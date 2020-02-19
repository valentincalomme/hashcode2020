from __future__ import annotations


class Solution:
    def __init__(self, problem_name: str, solver_name: str):

        self.problem_name = problem_name
        self.solver_name = solver_name

    def to_file(self) -> Path:
        """Persists the solution to a file

        Returns
        -------
        Path
            Relative path to the solution file
        """

        filename = f"{self.problem_name}_{self.solver_name}_{self.id}.solution"

    def is_valid(self) -> bool:
        """Checks whether the solution is valid

        Returns
        -------
        bool
            True if solution is valid, False if it isn't
        """
