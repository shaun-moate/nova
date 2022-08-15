#!/usr/bin/env python3

import subprocess
import sys
import os

from bin.common import uncons
from bin.help import usage

NOVA_EXT = ".nv"
SUCCESS = 0
FAIL = 0
FAILURE_LIST = []

def generate_all_test_cases(input_directory: str):
   assert os.path.isdir(input_directory), "ERROR: path must be a directory"
   for file in os.listdir(input_directory):
       f = os.path.join(input_directory, file)
       if os.path.isfile(f) and f.endswith(".nv"):
           generate_test_case(f)

def generate_test_case(input_file_path: str):
    output_file_path = str(input_file_path[:-len(NOVA_EXT)])
    print("[INFO] building %s: build/output" % (input_file_path))
    build = subprocess.run(["./nova.py", "-c", input_file_path], stdout=subprocess.DEVNULL)
    print("[INFO] generating test case file: %s -> %s" % (input_file_path, output_file_path))
    result = subprocess.run(["build/output"], capture_output=True, text=True)
    with open(output_file_path, "w") as file:
        file.write(":returncode %s\n" % (result.returncode))
        file.write(":stdout %d\n%s" % (len(result.stdout), result.stdout))

def run_all_test_cases(input_directory: str):
   assert os.path.isdir(input_directory), "ERROR: path must be a directory"
   for file in os.listdir(input_directory):
       f = os.path.join(input_directory, file)
       if os.path.isfile(f) and f.endswith(".nv"):
           run_test_case(f)
   print("[INFO] all tests have concluded: SUCCESS = %d, FAILURES = %d" % (SUCCESS, FAIL))
   if len(FAILURE_LIST) > 0:
       print("[INFO] for reference, following test cases failed:\n%s" % (FAILURE_LIST))
       exit(1)

def run_test_case(input_file_path: str):
   global SUCCESS
   global FAIL
   global FAILURE_LIST
   print("[INFO] running test case: %s == %s" % (input_file_path, str(input_file_path[:-len(NOVA_EXT)])))
   if compile_test_case(input_file_path) == load_test_case(input_file_path):
      print("[PASS] test case PASSED: %s" % (input_file_path))
      SUCCESS += 1
   else:
      print("[FAIL] test case FAILED: %s" % (input_file_path))
      FAIL += 1
      FAILURE_LIST.append(input_file_path)

def compile_test_case(input_file_path: str):
    build = subprocess.run(["./nova.py", "-c", input_file_path], stdout=subprocess.DEVNULL)
    result = subprocess.run(["build/output"], capture_output=True, text=True)
    return str(result.returncode) + result.stdout

def load_test_case(input_file_path: str):
    test_case_file_path = str(input_file_path[:-len(NOVA_EXT)])
    with open(test_case_file_path, "r") as file:
       while True:
          line = file.readline()
          if line.startswith(":returncode"):
             returncode = line[-2]
          elif line.startswith(":stdout"):
             stdout_len = int(line[8:-1])
             stdout = file.read(stdout_len)
          elif not line:
             break
       return returncode + stdout

if __name__ == '__main__':
    argv = sys.argv
    assert len(argv) >= 1
    (program, argv) = uncons(argv)
    if len(argv) < 1:
        print("ERROR: no subcommand has been provided")
        usage(program)
    (subcommand, argv) = uncons(argv)
    if subcommand == "--generate" or subcommand == "-g":
        if len(argv) < 1:
            print("ERROR: no input directory to generate test cases")
            usage(program)
        (input_directory, argv) = uncons(argv)
        generate_all_test_cases(input_directory)
    elif subcommand == "--run" or subcommand == "-r":
        if len(argv) < 1:
            print("ERROR: no input directory to run test cases")
            usage(program)
        (input_directory, argv) = uncons(argv)
        ## run_all_test_cases(input_directory)
        run_all_test_cases(input_directory)
    elif subcommand == "--help":
        usage(program)
    else:
        print("ERROR: unknown nova subcommand '%s'" % (subcommand))
        usage(program)
