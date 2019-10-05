#!/usr/bin/env python3

""" tigersatgenerator/dimacs.py
        Generates CNF output in standard DIMACS format. """

from typing import List, Set
import datetime


def get_clauses_statistics(clauses: List[List[int]]) -> (int, int):
    '''

    Args:
        clauses: A clause list in CNF.

    Returns:
        A tuple of (num_clauses, num_variables)
    '''
    variable_set: Set[int] = set(abs(literal) for clause in clauses for literal in clause)
    return len(clauses), len(variable_set)


def print_as_dimacs_cnf(clauses: List[List[int]], comment: str = None) -> None:
    '''

    Args:
        clauses: The clauses to print out in CNF.
        comment: A single-line comment; multi-line comments will break formatter

    Returns:
        None
    '''

    if comment is not None and comment.contains("\n"):
        raise Exception("comment must be a single-line string")

    # Start with a comment
    if comment is None:
        comment = "CNF generated on " + str(datetime.datetime.now())
    print("c " + comment)

    # Print standard CNF statistics
    (num_clauses, num_variables) = get_clauses_statistics(clauses)
    print("p cnf " + str(num_clauses) + " " + str(num_variables))

    # Now print each clauses
    for clause in clauses:
        line = " ".join(str(variable) for variable in clause)
        line = line + "0"  # lines are 0-terminated
        print(line)
