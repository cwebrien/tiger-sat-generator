#!/usr/bin/env python3

""" tigersatgenerator/__main__.py
        Stand-alone CLI for generating SAT problems in DIMACS format. """


from typing import List
import sys
import uniformksat.generator as ksatgen
import dimacs


def __get_generator_types() -> List[str]:
    return [
        "uniform-ksat"
    ]


def print_general_usage() -> None:
    print("Usage:")
    print(" python tigersatgenerator generator_type <generator_specific_args>")
    print("")
    print("Generator types are: " + str(__get_generator_types()))


def print_ksat_usage() -> None:
    print("Usage:")
    print(" python tigersatgenerator uniform-ksat k num_clauses num_variables")


def execute_from_arguments(args: List[str]) -> None:
    if len(args) <= 1 or args[1] not in [
        "uniform-ksat"
    ]:
        print_general_usage()
        return

    if args[1] == "uniform-ksat":
        if len(args) == 5:
            clauses = ksatgen.random_ksat_clauses(int(args[2]), int(args[3]), int(args[4]))
            dimacs.print_as_dimacs_cnf(clauses)
        else:
            print_ksat_usage()


def main():
    execute_from_arguments(sys.argv)


if __name__ == "__main__":
    main()
