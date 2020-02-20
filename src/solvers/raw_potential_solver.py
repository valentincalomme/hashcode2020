from __future__ import annotations

from solution import Solution
from solvers import Solver


class RawPotentialSolver(Solver):
    """Sorts libraries based on greedy criteria, then
    for each library, the books are sorted accordingly"""

    def yield_solutions(self, problem: Problem) -> Solution:

        # start with library with shortest sign up time

        day = 0

        scanned_books = set()
        libs = []

        while day < problem.num_days:

            if problem.libraries == []:
                break

            problem.libraries = sorted(
                problem.libraries,
                key=lambda x: x.potential(time=day, deadline=problem.num_days),
                reverse=True,
            )
            library = problem.libraries.pop(0)

            day += library.sign_up_time

            books_worth_scanning = list(set(library.books).difference(scanned_books))
            books_worth_scanning = sorted(
                books_worth_scanning, key=lambda x: x.book_score, reverse=True
            )
            books_worth_scanning = books_worth_scanning[
                : (problem.num_days - day) * library.books_per_day
            ]

            if len(books_worth_scanning) > 0:

                scanned_books = scanned_books.union(set(books_worth_scanning))
                library.books_to_scan = books_worth_scanning

                libs.append(library)

        solution = Solution(problem_name=problem.name, libraries=libs)

        yield solution
