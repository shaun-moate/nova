import subprocess

def uncons(xs):
    return (xs[0], xs[1:])

def find_next(line: str, start: int, predicate) -> int:
    while start < len(line) and not predicate(line[start]):
        start += 1
    return start

def get_macro_or_const_name(line: str, start: int):
    skip_end = find_next(line, start, lambda x: x.isspace())
    if line[start:skip_end] == "macro" or line[start:skip_end] == "const":
        start_next = find_next(line, skip_end+1, lambda x: not x.isspace())
        end_next = find_next(line, start_next, lambda x: x.isspace())
        return (line[start_next:end_next], start_next, end_next)
    else:
        assert False, "ERROR: get_macro_or_const_name must be called on a 'macro' or a 'const'"

def call_cmd():
    print("BUILD:-------------------------------------")
    print("run: nasm -felf64 build/output.asm")
    subprocess.call(["nasm", "-felf64", "build/output.asm"])
    print("run: ld -o build/output build/output.o")
    subprocess.call(["ld", "-o", "build/output", "build/output.o"])
    print("run: build/output")
    print("-------------------------------------------")

def usage(program):
    print("-------------------------------------------")
    print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
    print("SUBCOMMANDS:")
    print("    --compile  (-c) <file>       Compile the program to Assembly")
    print("    --help                       Provide usage details")
    print("    --simulate (-s) <file>       Simulate the program using Python3")
    print("-------------------------------------------")
    exit(1)

