from __future__ import annotations

import uuid
import os


class Solution:
    """Represents the solution to the instance of a problem"""

    def __init__(self, problem_name: str, libraries: List[Library]):

        self.solution_id = str(uuid.uuid4())
        self.problem_name = problem_name
        self.libraries = libraries
        self.scanned_books = {}

    def add_library(self, library: Library, time: int) -> Solution:

        library.sign_up_day = time
        self.libraries.append(library)
        self.books.union(set(library.books))

        return self

    def serialize(self) -> str:

        raw = f"{len(self.libraries)}\n"

        for library in self.libraries:

            raw += f"{library.library_id} {len(library.books_to_scan)}\n"
            raw += " ".join([str(book.book_id) for book in library.books_to_scan]) + "\n"

        return raw

    def to_file(self) -> Path:
        """Persists the solution to a file

        Returns
        -------
        Path
            Relative path to the solution file
        """

        filename = f"../data/solutions/{self.problem_name}.{self.solution_id}.solution"

        with open(filename, "w", encoding="utf-8") as file:

            file.write(self.serialize())

        return filename
