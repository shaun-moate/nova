#!/usr/bin/env python3

import subprocess
import sys

from bin.common import uncons

def create_test_result_for_file(input_file_path: str):
    output_file_path = str(input_file_path[:-3])
    output = subprocess.run(["./nova.py", "-c", input_file_path])
    print("[INFO] saving output of %s to %s" % (input_file_path, output_file_path))
    with open(output_file_path, "w") as file:
        subprocess.call(["./nova.py", "-c", input_file_path], stdout=file)

if __name__ == '__main__':
    argv = sys.argv
    assert len(argv) >= 1
    (program, argv) = uncons(argv)
    if len(argv) < 1:
        print("ERROR: no subcommand has been provided")
    (subcommand, argv) = uncons(argv)
    if subcommand == "--file" or subcommand == "-f":
        if len(argv) < 1:
            print("ERROR: no input file provided to simulation")
        (input_file_path, argv) = uncons(argv)
        create_test_result_for_file(input_file_path)
    else:
        print("ERROR: unknown nova subcommand '%s'" % (subcommand))
        usage(program)
