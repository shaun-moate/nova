#!/usr/bin/env python3

def usage(program):
    print("-------------------------------------------")
    print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
    print("SUBCOMMANDS:")
    print("    --compile  (-c) <file>       Compile the program")
    print("    --help          <file>       Provide usage details")
    print("    --simulate (-s) <file>       Simulate the program")
    print("-------------------------------------------")
    exit(1)
