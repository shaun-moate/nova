#!/usr/bin/env python3

def usage(program):
    print("-------------------------------------------")
    print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
    print("SUBCOMMANDS:")
    print("    --compile  (-c) <file>       Compile to Assembly && Run the program")
    print("    --help          <file>       Provide usage details")
    print("    --simulate (-s) <file>       Simulate the program using Python3")
    print("-------------------------------------------")
    exit(1)
