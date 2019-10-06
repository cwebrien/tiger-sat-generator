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


def get_dimacs_cnf(clauses: List[List[int]], comment: str = None) -> str:
    '''
        Produces a DIMACS-formatted string of a CNF list of clauses.
        Args:
            clauses: The clauses to print out in CNF.
            comment: A single-line comment; multi-line comments will break formatter

        Returns:
            String of CNF in DIMACS format.
        '''

    if "\n" in comment:
        raise Exception("comment must be a single-line string")

    result: str = ""

    # Start with a comment
    if comment is None:
        comment = "CNF generated on " + str(datetime.datetime.now())
    result = "c " + comment + "\n"

    # Print standard CNF statistics
    (num_clauses, num_variables) = get_clauses_statistics(clauses)
    result = result + "p cnf " + str(num_clauses) + " " + str(num_variables) + "\n"

    # Now print each clauses
    for clause in clauses:
        line = " ".join(str(variable) for variable in clause)
        line = line + " 0"  # lines are 0-terminated
        result = result + line + "\n"

    return result


def print_as_dimacs_cnf(clauses: List[List[int]], comment: str = None) -> None:
    '''
    Prints a CNF formulae from a list of clauses in DIMACS-formatted text.
    Args:
        clauses: The clauses to print out in CNF.
        comment: A single-line comment; multi-line comments will break formatter

    Returns:
        None
    '''
    to_print: str = get_dimacs_cnf(clauses, comment)
    print(to_print)
