#!/usr/bin/env python3

""" tigersatgenerator/tests/test_uniformksat_generator.py
        Tests for our random k-SAT generator. """

import tigersatgenerator.uniformksat.generator as ksatgen


class TestUniformKSat:
    def test_random_ksat_clauses(self) -> None:
        '''
        Tests our creation of random k-SAT clause lists.
        Returns:
        '''

        # Basic test cases as (k, num_clauses, num_variables)
        test_cases = [
            (1, 5, 3),
            (2, 5, 3),
            (3, 5, 3),
            (3, 1, 3)
        ]
        for (k, num_clauses, num_variables) in test_cases:
            clauses = ksatgen.random_ksat_clauses(k, num_clauses, num_variables)
            assert(num_clauses == len(clauses))
            for clause in clauses:
                assert(k == len(clause))
