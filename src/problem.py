from __future__ import annotations


class Problem:
    """Problem to solve"""

    def __init__(self, name: str, filename: Path):

        self.name = name
        self.filename = filename

        with open(self.filename, "r", encoding="utf-8") as file:

            self.raw = file.read()

        self.parse()

    def parse(self, raw: str):
        """Parses the raw representation of the problem

        Parameters
        ----------
        raw : str
            text representation of the problem
        """

        raise NotImplementedError
