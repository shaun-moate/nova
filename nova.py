#!/usr/bin/env python3
import sys
import subprocess

import bin.config as cfg
from bin.common import uncons, iota
from bin.help import usage
from bin.lexer import parse_program_from_file

cfg.OP_PUSH      = iota(True)
cfg.OP_DROP      = iota()
cfg.OP_PLUS      = iota()
cfg.OP_MINUS     = iota()
cfg.OP_MULT      = iota()
cfg.OP_EQUAL     = iota()
cfg.OP_NOT_EQUAL = iota()
cfg.OP_GREATER   = iota()
cfg.OP_GR_EQ     = iota()
cfg.OP_LESSER    = iota()
cfg.OP_LESS_EQ   = iota()
cfg.OP_IF        = iota()
cfg.OP_ELSE      = iota()
cfg.OP_END       = iota()
cfg.OP_WHILE     = iota()
cfg.OP_DO        = iota()
cfg.OP_DUPLICATE = iota()
cfg.OP_MEM_ADDR  = iota()
cfg.OP_MEM_STORE = iota()
cfg.OP_MEM_LOAD  = iota()
cfg.OP_SYSCALL   = iota()
cfg.OP_DUMP      = iota()
cfg.OP_EXIT      = iota()
cfg.OP_COUNT     = iota()

def simulate_program(program):
    stack = []
    mem = bytearray(cfg.MEM_ALLOCATION_SIZE)
    ip = 0
    print("RESULTS:-----------------------------------")
    while ip < len(program):
        assert cfg.OP_COUNT == 23, "Exhaustive list of operands in simulate_program()"
        op = program[ip]
        if op['action'] == cfg.OP_PUSH:
            stack.append(op['value'])
            ip += 1
        elif op['action'] == cfg.OP_DROP:
            stack.pop()
            ip += 1
        elif op['action'] == cfg.OP_DUMP:
            x = stack.pop()
            print(x)
            ip += 1
        elif op['action'] == cfg.OP_DUPLICATE:
            x = stack.pop()
            stack.append(x)
            stack.append(x)
            ip += 1
        elif op['action'] == cfg.OP_PLUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
            ip += 1
        elif op['action'] == cfg.OP_MINUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
            ip += 1
        elif op['action'] == cfg.OP_MULT:
            x = stack.pop()
            y = stack.pop()
            stack.append(y * x)
            ip += 1
        elif op['action'] == cfg.OP_EQUAL:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y == x))
            ip += 1
        elif op['action'] == cfg.OP_NOT_EQUAL:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y != x))
            ip += 1
        elif op['action'] == cfg.OP_GREATER:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y > x))
            ip += 1
        elif op['action'] == cfg.OP_GR_EQ:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y >= x))
            ip += 1
        elif op['action'] == cfg.OP_LESSER:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y < x))
            ip += 1
        elif op['action'] == cfg.OP_LESS_EQ:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y <= x))
            ip += 1
        elif op['action'] == cfg.OP_IF:
            assert len(op) > 1, "ERROR: 'if' block has no referenced 'else' or 'end'"
            if stack.pop() == 0:
                ip = op['jump_to']
            else:
                ip += 1
        elif op['action'] == cfg.OP_ELSE:
            assert len(op) > 1, "ERROR: 'else' block has no referenced 'end'"

        elif op['action'] == cfg.OP_DO:
            ip += 1
        elif op['action'] == cfg.OP_WHILE:
            assert len(op) > 1, "ERROR: 'do' block has no referenced 'end'"
            if stack.pop() == 0:
                ip = op['jump_to']
            else:
                ip += 1
        elif op['action'] == cfg.OP_END:
            ip = op['jump_to']
        elif op['action'] == cfg.OP_MEM_ADDR:
            stack.append(0)
            ip += 1
        elif op['action'] == cfg.OP_MEM_STORE:
            byte = stack.pop()
            addr = stack.pop()
            mem[addr] = byte
            ip += 1
        elif op['action'] == cfg.OP_MEM_LOAD:
            addr = stack.pop()
            byte = mem[addr]
            stack.append(byte)
            ip += 1
        elif op['action'] == cfg.OP_SYSCALL:
            syscall_num = stack.pop()
            arg1 = stack.pop()
            arg2 = stack.pop()
            arg3 = stack.pop()
            if syscall_num == 1:
                print(mem[:arg3].decode('utf-8'), end="")
            ip += 1
        elif op['action'] == cfg.OP_EXIT:
            x = stack.pop()
            exit(x)
            ip += 1
        else:
            assert False, "Operands is unreachable"
    print("\n-------------------------------------------")

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
        for ip in range(len(program)):
            assert cfg.OP_COUNT == 23, "Exhaustive list of operands in compile_program()"
            op = program[ip]
            out.write("addr_%d:\n" % ip)
            if op['action'] == cfg.OP_PUSH:
                out.write("    push %d\n" % op['value'])
            elif op['action'] == cfg.OP_DROP:
                out.write("    pop rax\n")
            elif op['action'] == cfg.OP_DUMP:
                out.write("    pop rdi\n")
                out.write("    call dump\n")
            elif op['action'] == cfg.OP_PLUS:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    add rax, rbx\n")
                out.write("    push rax\n")
            elif op['action'] == cfg.OP_DUPLICATE:
                out.write("    pop rax\n")
                out.write("    push rax\n")
                out.write("    push rax\n")
            elif op['action'] == cfg.OP_MINUS:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    sub rbx, rax\n")
                out.write("    push rbx\n")
            elif op['action'] == cfg.OP_MULT:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    mul rbx\n")
                out.write("    push rax\n")
            elif op['action'] == cfg.OP_EQUAL:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rax, rbx\n")
                out.write("    cmove rcx, rdx\n")
                out.write("    push rcx\n")
            elif op['action'] == cfg.OP_NOT_EQUAL:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rax, rbx\n")
                out.write("    cmovne rcx, rdx\n")
                out.write("    push rcx\n")
            elif op['action'] == cfg.OP_GREATER:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovg rcx, rdx\n")
                out.write("    push rcx\n")
            elif op['action'] == cfg.OP_GR_EQ:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovge rcx, rdx\n")
                out.write("    push rcx\n")
            elif op['action'] == cfg.OP_LESSER:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovl rcx, rdx\n")
                out.write("    push rcx\n")
            elif op['action'] == cfg.OP_LESS_EQ:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovle rcx, rdx\n")
                out.write("    push rcx\n")
            elif op['action'] == cfg.OP_IF:
                assert len(op) > 1, "ERROR: 'if' block has no referenced 'end'"
                out.write("    pop rax\n")
                out.write("    test rax, rax\n")
                out.write("    jz addr_%d\n" % op['jump_to'])
            elif op['action'] == cfg.OP_ELSE:
                out.write("    jmp addr_%d\n" % op['jump_to'])
            elif op['action'] == cfg.OP_DO:
                pass
            elif op['action'] == cfg.OP_WHILE:
                assert len(op) > 1, "ERROR: 'do' block has no referenced 'end'"
                out.write("    pop rax\n")
                out.write("    test rax, rax\n")
                out.write("    jz addr_%d\n" % op['jump_to'])
            elif op['action'] == cfg.OP_END:
                out.write("    jmp addr_%d\n" % op['jump_to'])
            elif op['action'] == cfg.OP_MEM_ADDR:
                out.write("    push mem\n")
            elif op['action'] == cfg.OP_MEM_STORE:
                out.write("    pop rbx\n")
                out.write("    pop rax\n")
                out.write("    mov [rax], bl\n")
            elif op['action'] == cfg.OP_MEM_LOAD:
                out.write("    pop rax\n")
                out.write("    xor rbx, rbx\n")
                out.write("    mov bl, [rax]\n")
                out.write("    push rbx\n")
            elif op['action'] == cfg.OP_SYSCALL:
                out.write("    pop rax\n")
                out.write("    pop rdi\n")
                out.write("    pop rsi\n")
                out.write("    pop rdx\n")
                out.write("    syscall\n")
            elif op['action'] == cfg.OP_EXIT:
                out.write("    mov rax, 60\n")
                out.write("    pop rdi\n")
                out.write("    syscall\n")
            else:
                assert False, "Operands is unreachable"
        out.write("addr_%d:\n" % len(program))
        out.write("    mov rax, 60\n")
        out.write("    mov rdi, 0\n")
        out.write("    syscall\n")
        out.write("segment .bss\n")
        out.write("mem: resb %d\n" % cfg.MEM_ALLOCATION_SIZE)
        out.close()
        call_cmd()

def call_cmd():
    print("BUILD:-------------------------------------")
    print("run: nasm -felf64 build/output.asm")
    subprocess.call(["nasm", "-felf64", "build/output.asm"])
    print("run: ld -o build/output build/output.o")
    subprocess.call(["ld", "-o", "build/output", "build/output.o"])
    print("run: build/output")
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
        program = parse_program_from_file(input_file_path)
        simulate_program(program)
    elif subcommand == "--compile" or subcommand == "-c":
        if len(argv) > 1:
            (option, argv) = uncons(argv)
            if option == "--run" or option == "-r":
                (input_file_path, argv) = uncons(argv)
                program = parse_program_from_file(input_file_path)
                compile_program(program)
                subprocess.call(["build/output"])
        elif len(argv) <= 1:
            (input_file_path, argv) = uncons(argv)
            program = parse_program_from_file(input_file_path)
            compile_program(program)
        elif len(argv) < 1:
            print("ERROR: no input file provided to compilation")
            usage(program)
    elif subcommand == "--help":
        usage(program)
    else:
        print("ERROR: unknown nova subcommand '%s'" % (subcommand))
        usage(program)
