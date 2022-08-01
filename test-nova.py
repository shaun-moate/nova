#!/usr/bin/env python3

import subprocess
import sys
import os

from bin.common import uncons

NOVA_EXT = ".nv"

def save_test_cases_in_directory(input_directory: str):
   assert os.path.isdir(input_directory), "ERROR: path must be a directory"
   for file in os.listdir(input_directory):
       f = os.path.join(input_directory, file)
       if os.path.isfile(f) and f.endswith(".nv"):
           save_test_case_for_file(f)

def save_test_case_for_file(input_file_path: str):
    output_file_path = str(input_file_path[:-len(NOVA_EXT)])
    print("[INFO] saving stdout of %s to %s" % (input_file_path, output_file_path))
    with open(output_file_path, "w") as file:
        subprocess.call(["./nova.py", "-c", input_file_path], stdout=open(os.devnull, "w"))
        subprocess.call(["build/output"], stdout=file)

if __name__ == '__main__':
    argv = sys.argv
    assert len(argv) >= 1
    (program, argv) = uncons(argv)
    if len(argv) < 1:
        print("ERROR: no subcommand has been provided")
    (subcommand, argv) = uncons(argv)
    if subcommand == "--dir" or subcommand == "-d":
        if len(argv) < 1:
            print("ERROR: no input file provided to simulation")
        (input_directory, argv) = uncons(argv)
        save_test_cases_in_directory(input_directory)
    elif subcommand == "--file" or subcommand == "-f":
        if len(argv) < 1:
            print("ERROR: no input file provided to simulation")
        (input_file_path, argv) = uncons(argv)
        save_test_case_for_file(input_file_path)
    else:
        print("ERROR: unknown nova subcommand '%s'" % (subcommand))
