#!/usr/bin/env python3
import sys
import subprocess

iota_counter = 0
def iota(reset=False):
    global iota_counter
    if reset == True:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

OP_PUSH  = iota(True)
OP_PLUS  = iota()
OP_MINUS = iota()
OP_DUMP = iota()
OP_COUNT = iota()

def push(value):
    return (OP_PUSH, value)

def plus():
    return (OP_PLUS, )

def minus():
    return (OP_MINUS, )

def dump():
    return (OP_DUMP, )

def simulate_program(program):
    stack = []
    for op in program:
        assert OP_COUNT == 4, "Exhaustive list of operands in emulate_program()"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif op[0] == OP_MINUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif op[0] == OP_DUMP:
            x = stack.pop()
            print(x)
        else:
            assert False, "Operands is unreachable"


def compile_program(program):
    with open("output.asm", "w") as out:
        out.write("segment .text\n")

        out.write("dump:\n")
        out.write("    mov r9, -3689348814741910323\n")
        out.write("    sub rsp, 40\n")
        out.write("    mov BYTE [rsp+31], 10\n")
        out.write("    lea rcx, [rsp+30]\n")
        out.write(".L2:\n")
        out.write("    mov rax, rdi\n")
        out.write("    lea r8, [rsp+32]\n")
        out.write("    mul r9\n")
        out.write("    mov rax, rdi\n")
        out.write("    sub r8, rcx\n")
        out.write("    shr rdx, 3\n")
        out.write("    lea rsi, [rdx+rdx*4]\n")
        out.write("    add rsi, rsi\n")
        out.write("    sub rax, rsi\n")
        out.write("    add eax, 48\n")
        out.write("    mov BYTE [rcx], al\n")
        out.write("    mov rax, rdi\n")
        out.write("    mov rdi, rdx\n")
        out.write("    mov rdx, rcx\n")
        out.write("    sub rcx, 1\n")
        out.write("    cmp rax, 9\n")
        out.write("    ja  .L2\n")
        out.write("    lea rax, [rsp+32]\n")
        out.write("    mov edi, 1\n")
        out.write("    sub rdx, rax\n")
        out.write("    xor eax, eax\n")
        out.write("    lea rsi, [rsp+32+rdx]\n")
        out.write("    mov rdx, r8\n")
        out.write("    mov rax, 1\n")
        out.write("    syscall\n")
        out.write("    add rsp, 40\n")
        out.write("    ret\n")

        out.write("global _start\n_start:\n")
        for op in program:
            assert OP_COUNT == 4, "Exhaustive list of operands in emulate_program()"
            if op[0] == OP_PUSH:
                out.write("    push %d\n" % op[1])
            elif op[0] == OP_PLUS:
                out.write("    pop rax\n    pop rbx\n    add rax, rbx\n    push rax\n")
            elif op[0] == OP_MINUS:
                out.write("    pop rax\n    pop rbx\n    sub rbx, rax\n    push rbx\n")
            elif op[0] == OP_DUMP:
                out.write("    pop rdi\n    call dump\n")
            else:
                assert False, "Operands is unreachable"
        out.write("    mov rax, 60\n    mov rdi, 0\n    syscall")
        out.close()
        subprocess.call(["nasm", "-felf64", "output.asm"])
        subprocess.call(["ld", "-o", "output", "output.o"])

def parse_program_from_file(input_file_path):
    with open(input_file_path, "r") as f:
        return [parse_token_as_op(token) for token in f.read().split()]

def parse_token_as_op(token):
    assert OP_COUNT == 4, "Exhaustive list of operands in emulate_program()"
    if token == "+":
        return plus()
    elif token == "-":
        return minus()
    elif token == "print":
        return dump()
    elif isinstance(int(token), int):
        return push(int(token))
    else:
        assert False, "Operand is unreachable"

def nova_usage():
    print("-------------------------------------------")
    print("Usage: nova <SUBCOMMAND> [ARGS]")
    print("SUBCOMMANDS:")
    print("    simulate <file>       Simulate the program")
    print("    compile  <file>       Compile the program")
    print("-------------------------------------------")
    exit(1)


def uncons(xs):
    return (xs[0], xs[1:])

if __name__ == '__main__':
    argv = sys.argv
    assert len(argv) >= 1
    (program, argv) = uncons(argv)
    if len(argv) < 1:
        print("ERROR: no subcommand has been provided")
        nova_usage()
    (subcommand, argv) = uncons(argv)
    if subcommand == "simulate":
        if len(argv) < 1:
            print("ERROR: no input file provided to simulation")
            nova_usage()
        (input_file_path, argv) = uncons(argv)
        program = parse_program_from_file(input_file_path)
        simulate_program(program)
    elif subcommand == "compile":
        if len(argv) < 1:
            print("ERROR: no input file provided to compilation")
            nova_usage()
        (input_file_path, argv) = uncons(argv)
        program = parse_program_from_file(input_file_path)
        compile_program(program)
    else:
        print("ERROR: unknown nova subcommand '%s'" % (subcommand))
        nova_usage()
