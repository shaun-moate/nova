#!/usr/bin/env python3
import sys
import subprocess

import bin.config as cfg
from bin.common import uncons, iota
from bin.help import usage
from bin.lexer import parse_program_from_tokens

cfg.OP_PUSH      = iota(True)
cfg.OP_PLUS      = iota()
cfg.OP_MINUS     = iota()
cfg.OP_DUMP      = iota()
cfg.OP_COUNT     = iota()

def simulate_program(program):
    stack = []
    for op in program:
        assert cfg.OP_COUNT == 4, "Exhaustive list of operands in emulate_program()"
        if op[0] == cfg.OP_PUSH:
            stack.append(op[1])
        elif op[0] == cfg.OP_PLUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif op[0] == cfg.OP_MINUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif op[0] == cfg.OP_DUMP:
            x = stack.pop()
            print(x)
        else:
            assert False, "Operands is unreachable"


def compile_program(program):
    with open("build/output.asm", "w") as out:
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
            assert cfg.OP_COUNT == 4, "Exhaustive list of operands in emulate_program()"
            if op[0] == cfg.OP_PUSH:
                out.write("    push %d\n" % op[1])
            elif op[0] == cfg.OP_PLUS:
                out.write("    pop rax\n    pop rbx\n    add rax, rbx\n    push rax\n")
            elif op[0] == cfg.OP_MINUS:
                out.write("    pop rax\n    pop rbx\n    sub rbx, rax\n    push rbx\n")
            elif op[0] == cfg.OP_DUMP:
                out.write("    pop rdi\n    call dump\n")
            else:
                assert False, "Operands is unreachable"
        out.write("    mov rax, 60\n    mov rdi, 0\n    syscall")
        out.close()
        call_cmd()

def call_cmd():
    print("BUILD:-------------------------------------")
    print("run: nasm -felf64 build/output.asm")
    subprocess.call(["nasm", "-felf64", "build/output.asm"])
    print("run: ld -o build/output build/output.o")
    subprocess.call(["ld", "-o", "build/output", "build/output.o"])
    print("RESULTS:-----------------------------------")
    print("run: build/output")
    subprocess.call(["build/output"])
    print("-------------------------------------------")

if __name__ == '__main__':
    argv = sys.argv
    assert len(argv) >= 1
    (program, argv) = uncons(argv)
    if len(argv) < 1:
        print("ERROR: no subcommand has been provided")
        usage(program)
    (subcommand, argv) = uncons(argv)
    if subcommand == "--simulate" or subcommand == "-s":
        if len(argv) < 1:
            print("ERROR: no input file provided to simulation")
            usage(program)
        (input_file_path, argv) = uncons(argv)
        program = parse_program_from_tokens(input_file_path)
        simulate_program(program)
    elif subcommand == "--compile" or subcommand == "-c":
        if len(argv) < 1:
            print("ERROR: no input file provided to compilation")
            usage(program)
        (input_file_path, argv) = uncons(argv)
        program = parse_program_from_tokens(input_file_path)
        compile_program(program)
    elif subcommand == "--help":
        usage(program)
    else:
        print("ERROR: unknown nova subcommand '%s'" % (subcommand))
        usage(program)
