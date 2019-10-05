#!/usr/bin/env python3

""" tigersatgenerator.uniformksat.generator.py
        Generates k-SAT formulae in the standard DIMACS format. """

from typing import List
import random


def random_ksat_clauses(k: int, num_clauses: int, num_variables: int, seed: int = None) -> List[List[int]]:
    '''

    Args:
        k: Number of literals per clause
        num_clauses: Number of clauses to generate
        num_variables: Number of variables across all clauses
        seed: Optional seed for reproducibility of results

    Returns: A list of clauses where each clause itself is a list

    '''
    if k <= 0:
        raise Exception("k-SAT requires k >= 1, although trivial for k = 1")

    if num_clauses <= 0:
        raise Exception("k-SAT requires num_clauses >=1")

    if num_variables < k:
        raise Exception("k-SAT requires num_variables >= k to generator clauses without repeated variables")

    clauses = []
    random.seed(seed)

    for clause_count in range(1, num_clauses):
        new_clause = []
        variables_used = {}    # only use a variable once in a clause
        literal_count = 0

        # Randomly select a variable and then randomly produce a literal (i.e. keep variable as is, or invert)
        while literal_count < k:
            # Randomly select a variable
            variable = random.randint(1, num_variables)

            # Use the variable if possible
            if variable not in variables_used:
                pos_or_neg = 1 if random.random() < 0.5 else -1  # produce a literal by possibly inverting
                new_clause.append(pos_or_neg * variable)

                variables_used[variable] = 1
                literal_count += 1

        clauses.append(new_clause)

    return clauses



