#!/usr/bin/env python3

def usage(program):
    if program == "./nova.py":
        print("-------------------------------------------")
        print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
        print("SUBCOMMANDS:")
        print("    --compile  (-c) <file>       Compile the program to Assembly")
        print("    --help                       Provide usage details")
        print("    --simulate (-s) <file>       Simulate the program using Python3")
        print("-------------------------------------------")
        exit(1)
    elif program == "./test-nova.py":
        print("-------------------------------------------")
        print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
        print("SUBCOMMANDS:")
        print("    --generate <dir>       Iterate through each test and store outputs")
        print("    --help                 Provide usage details")
        print("    --run      <dir>       Iterate through each test, providing back aggregate success/failures")
        print("-------------------------------------------")
        exit(1)
