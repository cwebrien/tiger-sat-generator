#!/usr/bin/env python3

""" tigersatgenerator/tests/test_dimacs.py
        Tests for our DIMACS generator / formatter. """


import io
import tigersatgenerator.dimacs as dimacs


class TestDimacsGenerator:
    def test_get_clauses_statistics(self) -> None:
        '''
        Ensure that we pull the correct statistics from a few test clauses
        Returns:
        '''
        # Tuple of {clause list, num_clauses, num_variables}
        test_cases = [
            ([[1, 2, 3]], 1, 3),                   # one clause
            ([[1, 2, 3], [4, 5, 6]], 2, 6),        # two clauses, no repeats
            ([[1, 2, 3], [2, 3, 4]], 2, 4),        # two clauses, two repeats
            ([[1, 2, 3], [4, 5, 6], []], 3, 6),    # three clauses, one empty, no repeats
            ([[1, 2, 3], [-1, 2, -3]], 2, 3)       # inverted variables aren't double-counted?
        ]
        for case in test_cases:
            (num_clauses, num_variables) = dimacs.get_clauses_statistics(case[0])
            assert(num_clauses == case[1])
            assert(num_variables == case[2])

    def test_get_dimacs_cnf(self) -> None:
        '''
        Some very basic sanity tests for the DIMACS string that is generated.
        Returns:
        '''
        test_clauses = [[1, 2, 3], [-4, 5, -6], [7, 8, -9]]
        dimacs_string = dimacs.get_dimacs_cnf(test_clauses, "Some comment")
        dimacs_lines = io.StringIO(dimacs_string)

        # We should start with the comment string
        line = dimacs_lines.readline()
        assert(line[0:2] == "c ")

        # File format descriptor
        line = dimacs_lines.readline()
        assert(line == "p cnf 3 9\n")  # We have 3 clauses and 9 variables

        # Check for proper formatting of next 3 rows
        line = dimacs_lines.readline()
        assert(line == "1 2 3 0\n")  # We have 3 clauses and 9 variables
        line = dimacs_lines.readline()
        assert(line == "-4 5 -6 0\n")  # We have 3 clauses and 9 variables
        line = dimacs_lines.readline()
        assert(line == "7 8 -9 0\n")  # We have 3 clauses and 9 variables
