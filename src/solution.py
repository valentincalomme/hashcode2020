from __future__ import annotations

import uuid
import os


class Solution:
    """Represents the solution to the instance of a problem"""

    def __init__(self, problem_name: str):

        self.solution_id = str(uuid.uuid4())
        self.problem_name = problem_name

    def serialize(self) -> str:

        raise NotImplementedError

    def is_valid(self) -> bool:
        """Checks whether the solution is valid

        Returns
        -------
        bool
            True if solution is valid, False if it isn't
        """

        raise NotImplementedError

    def to_file(self, score: int) -> Path:
        """Persists the solution to a file

        Returns
        -------
        Path
            Relative path to the solution file
        """

        filename = f"data/solutions/{self.problem_name}.{self.solution_id}.solution"

        with open(filename, "w", encoding="utf-8") as file:

            file.write(self.serialize())

        return filename
