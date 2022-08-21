#!/usr/bin/env python3
import sys
import subprocess

iota_counter = 0

def uncons(xs):
    return (xs[0], xs[1:])

def iota(reset=False):
    global iota_counter
    if reset == True:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

## TODO: Add OP_ASSERT to support testing framework - enabling us to ensure we can assert() the expected correct result
OP_PUSH_INT  = iota(True)
OP_PUSH_STR  = iota()
OP_OVER      = iota()
OP_SWAP      = iota()
OP_DUP       = iota()
OP_2DUP      = iota()
OP_DROP      = iota()
OP_DUMP      = iota()
OP_SHL       = iota()
OP_SHR       = iota()
OP_B_AND     = iota()
OP_B_OR      = iota()
OP_PLUS      = iota()
OP_MINUS     = iota()
OP_MULT      = iota()
OP_EQUAL     = iota()
OP_NOT_EQUAL = iota()
OP_GREATER   = iota()
OP_GR_EQ     = iota()
OP_LESSER    = iota()
OP_LESS_EQ   = iota()
OP_IF        = iota()
OP_ELSE      = iota()
OP_FI        = iota()
OP_WHILE     = iota()
OP_DO        = iota()
OP_DONE      = iota()
OP_END       = iota()
OP_MEM_ADDR  = iota()
OP_MEM_STORE = iota()
OP_MEM_LOAD  = iota()
OP_SYSCALL   = iota()
OP_EXIT      = iota()
OP_COUNT     = iota()

MACRO_WRITE  = iota(True)
MACRO_COUNT  = iota()

CONST_CATCH  = iota(True)
CONST_COUNT  = iota()

TOKEN_OP     = iota(True)
TOKEN_MACRO  = iota()
TOKEN_CONST  = iota()
TOKEN_INT    = iota()
TOKEN_STR    = iota()
TOKEN_COUNT  = iota()

STR_ALLOCATION_SIZE = 69_000
MEM_ALLOCATION_SIZE = 69_000

assert OP_COUNT == 33, "Exhaustive list of operands"
BUILTIN_OPS = {
    "+": OP_PLUS,
    "-": OP_MINUS,
    "*": OP_MULT,
    "==": OP_EQUAL,
    "!=": OP_NOT_EQUAL,
    ">": OP_GREATER,
    ">=": OP_GR_EQ,
    "<": OP_LESSER,
    "<=": OP_LESS_EQ,
    "if": OP_IF,
    "else": OP_ELSE,
    "fi": OP_FI,
    "while": OP_WHILE,
    "do": OP_DO,
    "done": OP_DONE,
    "end": OP_END,
    "mem": OP_MEM_ADDR,
    "store8": OP_MEM_STORE,
    "load8": OP_MEM_LOAD,
    "syscall": OP_SYSCALL,
    "over": OP_OVER,
    "swap": OP_SWAP,
    "dup": OP_DUP,
    "2dup": OP_2DUP,
    "dump": OP_DUMP,
    "drop": OP_DROP,
    "shl": OP_SHL,
    "shr": OP_SHR,
    "band": OP_B_AND,
    "bor": OP_B_OR,
    "exit": OP_EXIT
}

## TODO: add MACROS to examples to improve readability -> ie. rule110.nv
assert MACRO_COUNT == 1, "Exhaustive list of macros"
BUILTIN_MACRO = {
    "write": [1, 1, 'syscall'],
}

assert CONST_COUNT == 1, "Exhaustive list of constants"
BUILTIN_CONST = {
    "CATCH": 22,
}

def parse_token_as_op(token):
    location = token["location"]
    word = token["value"]
    assert TOKEN_COUNT == 5, "Exhaustive list of operands in parse_word()"
    if token["type"] == TOKEN_OP:
        if token["value"] in BUILTIN_OPS:
            return {"action": BUILTIN_OPS[token["value"]], "location": token["location"], "value": token["value"]}
        else:
            print("%s:%d:%d: ERROR: unknown operand `%s` found" % (token["location"] + (token["value"], )))
            exit(1)
    elif token["type"] == TOKEN_MACRO:
        macro = token["value"]
        return [{"action": action,
                 "location": "",
                 "value": value}
                for (action, value) in parse_macro(macro)]
    elif token["type"] == TOKEN_CONST:
        if token["value"] in BUILTIN_CONST:
            return {"action": OP_PUSH_INT, "location": token["location"], "value": int(BUILTIN_CONST[token["value"]])}
    elif token["type"] == TOKEN_INT:
        return {"action": OP_PUSH_INT, "location": token["location"], "value": token["value"]}
    elif token["type"] == TOKEN_STR:
        return {"action": OP_PUSH_STR, "location": token["location"], "value": token["value"]}
    else:
        assert False, "Token type is unreachable is unreachable"

def parse_macro(macro):
    instructions = BUILTIN_MACRO[macro]
    if macro in BUILTIN_MACRO:
        for i in instructions:
            if parse_word(i)[0] == TOKEN_OP:
                if i in BUILTIN_OPS:
                    yield(BUILTIN_OPS[i], i)
                else:
                    assert False, "ERROR: `%s` not found in BUILTIN_OPS" % i
            elif parse_word(i)[0] == TOKEN_INT:
                yield(OP_PUSH_INT, int(i))

def parse_program_from_file(input_file_path):
    with open(input_file_path, "r") as file:
        return generate_blocks(
                    [parse_token_as_op(token) for token in parse_tokens_from_file(input_file_path)]
                )

def parse_tokens_from_file(input_file_path):
    with open(input_file_path, "r") as file:
        return [{"type": token_type,
                 "location": (input_file_path, row+1, col+1),
                 "value": token_value}
                for (row, line) in enumerate(file.readlines())
                for (col, (token_type, token_value)) in parse_line(line.split("//")[0])]

def parse_line(line):
    start = find_next(line, 0, lambda x: not x.isspace())
    while start < len(line):
        if line[start] == "\"":
            end = find_next(line, start+1, lambda x: x == "\"")
            yield(start, parse_word(line[start+1:end], typ="str"))
        elif line[start:find_next(line, start, lambda x: x.isspace())] == "macro":
            (name, start, end) = parse_name(line, start)
            if name in BUILTIN_MACRO:
                print("ERROR: attempting to override a built-in macro `%s` - not permitted" % name)
                exit(1)
            (macro_stack, start, end) = parse_macro_stack(line, start, end)
            BUILTIN_MACRO[name] = macro_stack
            start = find_next(line, end+1, lambda x: not x.isspace())
        elif line[start:find_next(line, start, lambda x: x.isspace())] in BUILTIN_MACRO:
            end = find_next(line, start, lambda x: x.isspace())
            yield(start, parse_word(line[start:end], typ="macro"))
        elif line[start:find_next(line, start, lambda x: x.isspace())] == "const":
            (name, start, end) = parse_name(line, start)
            if name in BUILTIN_CONST:
                print("ERROR: attempting to override a built-in constant `%s` - not permitted" % name)
                exit(1)
            (value, start, end) = parse_const_int(line, start, end)
            BUILTIN_CONST[name] = value
        elif line[start:find_next(line, start, lambda x: x.isspace())] in BUILTIN_CONST:
            end = find_next(line, start, lambda x: x.isspace())
            yield(start, parse_word(line[start:end], typ="const"))
        else:
            end = find_next(line, start, lambda x: x.isspace())
            yield(start, parse_word(line[start:end]))
        start = find_next(line, end+1, lambda x: not x.isspace())

def parse_name(line, start):
    skip_end = find_next(line, start, lambda x: x.isspace())
    start_next = find_next(line, skip_end+1, lambda x: not x.isspace())
    end_next = find_next(line, start_next, lambda x: x.isspace())
    return (line[start_next:end_next], start_next, end_next)

def parse_macro_stack(line, start, end):
    macro_stack = []
    start = find_next(line, end+1, lambda x: not x.isspace())
    while line[start:find_next(line, start, lambda x: x.isspace())] != "end":
        end = find_next(line, start, lambda x: x.isspace())
        assert parse_word(line[start:end])[0] == TOKEN_OP or parse_word(line[start:end])[0] == TOKEN_INT, "ERROR: macro op value must be of type operation or integer"
        macro_stack.append(line[start:end])
        start = find_next(line, end+1, lambda x: not x.isspace())
    end = find_next(line, start, lambda x: x.isspace())
    return (macro_stack, start, end)

def parse_const_int(line, start, end):
    start = find_next(line, end+1, lambda x: not x.isspace())
    end = find_next(line, start, lambda x: x.isspace())
    value = line[start:end]
    assert int(value), "ERROR: const value must be of type integer"
    return (value, start, end)

def parse_word(token, typ=None):
    assert TOKEN_COUNT == 5, "Exhaustive list of operands in parse_word()"
    if typ == "str":
        return (TOKEN_STR, bytes(token, "utf-8").decode("unicode_escape"))
    elif typ == "macro":
        return (TOKEN_MACRO, token)
    elif typ == "const":
        return (TOKEN_CONST, token)
    else:
        try:
            return (TOKEN_INT, int(token))
        except ValueError:
            return (TOKEN_OP, token)

def find_next(line, start, predicate):
    while start < len(line) and not predicate(line[start]):
        start += 1
    return start

def unnest_program(program):
    result = []
    for i in range(len(program)):
        if type(program[i]) is list:
            for j in range(len(program[i])):
                result.append(program[i][j])
        else:
            result.append(program[i])
    return result

def generate_blocks(program):
    block = []
    program = unnest_program(program)
    for ip in range(len(program)):
        assert OP_COUNT == 33, "Exhaustive list of operands in generate_blocks() -> Note: only operands that generate a block need to be included."
        if program[ip]["action"] == OP_IF:
            block.append(ip)
        if program[ip]["action"] == OP_ELSE:
            ref = block.pop()
            assert program[ref]["action"] == OP_IF, "ERROR: `else` can only be used in `if` blocks"
            program[ref]["action"] = OP_IF
            program[ref]["jump_to"] = ip+1
            block.append(ip)
        if program[ip]["action"] == OP_FI:
            ref = block.pop()
            assert program[ref]["action"] == OP_IF or program[ref]["action"] == OP_ELSE, "ERROR: `fi` is expected to end the blocks for `if` or `else` only"
            program[ip]["jump_to"] = ip+1
            program[ref]["jump_to"] = ip
        if program[ip]["action"] == OP_WHILE:
            block.append(ip)
        if program[ip]["action"] == OP_DO:
            ref = block.pop()
            assert program[ref]["action"] == OP_WHILE, "ERROR: `do` can only be used in `while` blocks"
            program[ip]["jump_to"] = ref
            block.append(ip)
        if program[ip]["action"] == OP_DONE:
            ref = block.pop()
            program[ip]["jump_to"] = program[ref]["jump_to"]
            program[ref]["action"] = OP_DO
            program[ref]["jump_to"] = ip+1
        if program[ip]["action"] == OP_END:
           pass
    return program

def simulate_program(program):
    stack = []
    mem = bytearray(MEM_ALLOCATION_SIZE + STR_ALLOCATION_SIZE)
    str_addr_start = 0
    ip = 0
    while ip < len(program):
        assert OP_COUNT == 33, "Exhaustive list of operands in simulate_program()"
        op = program[ip]
        if op["action"] == OP_PUSH_INT:
            stack.append(op["value"])
            ip += 1
        elif op["action"] == OP_PUSH_STR:
            str_bytes = bytes(op["value"], "utf-8")
            str_length = len(str_bytes)
            if "address" not in op:
                op["address"] = str_addr_start
                for i in reversed(range(str_length)):
                    mem[str_addr_start+i] = str_bytes[i]
                str_addr_start += str_length
                assert str_addr_start <= STR_ALLOCATION_SIZE, "ERROR: String buffer overflow"
            stack.append(str_length)
            stack.append(op["address"])
            ip += 1
        elif op["action"] == OP_OVER:
            x = stack.pop()
            y = stack.pop()
            stack.append(y)
            stack.append(x)
            stack.append(y)
            ip += 1
        elif op["action"] == OP_SWAP:
            x = stack.pop()
            y = stack.pop()
            stack.append(x)
            stack.append(y)
            ip += 1
        elif op["action"] == OP_DROP:
            stack.pop()
            ip += 1
        elif op["action"] == OP_DUMP:
            x = stack.pop()
            print(x)
            ip += 1
        elif op["action"] == OP_DUP:
            x = stack.pop()
            stack.append(x)
            stack.append(x)
            ip += 1
        elif op["action"] == OP_2DUP:
            x = stack.pop()
            y = stack.pop()
            stack.append(y)
            stack.append(x)
            stack.append(y)
            stack.append(x)
            ip += 1
        elif op["action"] == OP_SHL:
            x = stack.pop()
            y = stack.pop()
            stack.append(y << x)
            ip += 1
        elif op["action"] == OP_SHR:
            x = stack.pop()
            y = stack.pop()
            stack.append(y >> x)
            ip += 1
        elif op["action"] == OP_B_AND:
            x = stack.pop()
            y = stack.pop()
            stack.append(y & x)
            ip += 1
        elif op["action"] == OP_B_OR:
            x = stack.pop()
            y = stack.pop()
            stack.append(y | x)
            ip += 1
        elif op["action"] == OP_PLUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
            ip += 1
        elif op["action"] == OP_MINUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
            ip += 1
        elif op["action"] == OP_MULT:
            x = stack.pop()
            y = stack.pop()
            stack.append(y * x)
            ip += 1
        elif op["action"] == OP_EQUAL:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y == x))
            ip += 1
        elif op["action"] == OP_NOT_EQUAL:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y != x))
            ip += 1
        elif op["action"] == OP_GREATER:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y > x))
            ip += 1
        elif op["action"] == OP_GR_EQ:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y >= x))
            ip += 1
        elif op["action"] == OP_LESSER:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y < x))
            ip += 1
        elif op["action"] == OP_LESS_EQ:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y <= x))
            ip += 1
        elif op["action"] == OP_IF:
            assert len(op) > 1, "ERROR: `if` block has no referenced `else` or `end`"
            if stack.pop() == 0:
                ip = op["jump_to"]
            else:
                ip += 1
        elif op["action"] == OP_ELSE:
            assert len(op) > 1, "ERROR: `else` block has no referenced `end`"
            ip = op["jump_to"]
        elif op["action"] == OP_FI:
            ip = op["jump_to"]
        elif op["action"] == OP_WHILE:
            ip += 1
        elif op["action"] == OP_DO:
            assert len(op) > 1, "ERROR: `while` block has no referenced `done`"
            if stack.pop() == 0:
                ip = op["jump_to"]
            else:
                ip += 1
        elif op["action"] == OP_DONE:
            ip = op["jump_to"]
            ip += 1
        elif op["action"] == OP_END:
            ip += 1
        elif op["action"] == OP_MEM_ADDR:
            stack.append(STR_ALLOCATION_SIZE)
            ip += 1
        elif op["action"] == OP_MEM_STORE:
            byte = stack.pop()
            addr = stack.pop()
            mem[addr] = byte & 0xFF
            ip += 1
        elif op["action"] == OP_MEM_LOAD:
            addr = stack.pop()
            byte = mem[addr]
            stack.append(byte)
            ip += 1
        elif op["action"] == OP_SYSCALL:
            syscall_num = stack.pop()
            arg1 = stack.pop()
            arg2 = stack.pop()
            arg3 = stack.pop()
            if syscall_num == 1:
                print(mem[arg2:arg2+arg3].decode("utf-8"), end="")
            ip += 1
        elif op["action"] == OP_EXIT:
            x = stack.pop()
            exit(x)
            ip += 1
        else:
            assert False, "Operands is unreachable"

def compile_program(program):
    str_stack = []
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
            assert OP_COUNT == 33, "Exhaustive list of operands in compile_program()"
            op = program[ip]
            out.write("addr_%d:\n" % ip)
            if op["action"] == OP_PUSH_INT:
                out.write("    push %d\n" % op["value"])
            elif op["action"] == OP_PUSH_STR:
                str_bytes = bytes(op["value"], "utf-8")
                out.write("    mov rax, %d\n" % len(bytes(op["value"], "utf-8")))
                out.write("    push rax\n")
                out.write("    push str_%d\n" % len(str_stack))
                str_stack.append(str_bytes)
            elif op["action"] == OP_OVER:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    push rbx\n")
                out.write("    push rax\n")
                out.write("    push rbx\n")
            elif op["action"] == OP_SWAP:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    push rax\n")
                out.write("    push rbx\n")
            elif op["action"] == OP_DROP:
                out.write("    pop rax\n")
            elif op["action"] == OP_DUMP:
                out.write("    pop rdi\n")
                out.write("    call dump\n")
            elif op["action"] == OP_DUP:
                out.write("    pop rax\n")
                out.write("    push rax\n")
                out.write("    push rax\n")
            elif op["action"] == OP_2DUP:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    push rbx\n")
                out.write("    push rax\n")
                out.write("    push rbx\n")
                out.write("    push rax\n")
            elif op["action"] == OP_SHL:
                out.write("    pop rcx\n")
                out.write("    pop rax\n")
                out.write("    shl rax, cl\n")
                out.write("    push rax\n")
            elif op["action"] == OP_SHR:
                out.write("    pop rcx\n")
                out.write("    pop rax\n")
                out.write("    shr rax, cl\n")
                out.write("    push rax\n")
            elif op["action"] == OP_B_AND:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    and rax, rbx\n")
                out.write("    push rax\n")
            elif op["action"] == OP_B_OR:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    or rax, rbx\n")
                out.write("    push rax\n")
            elif op["action"] == OP_PLUS:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    add rax, rbx\n")
                out.write("    push rax\n")
            elif op["action"] == OP_MINUS:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    sub rbx, rax\n")
                out.write("    push rbx\n")
            elif op["action"] == OP_MULT:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    mul rbx\n")
                out.write("    push rax\n")
            elif op["action"] == OP_EQUAL:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rax, rbx\n")
                out.write("    cmove rcx, rdx\n")
                out.write("    push rcx\n")
            elif op["action"] == OP_NOT_EQUAL:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rax, rbx\n")
                out.write("    cmovne rcx, rdx\n")
                out.write("    push rcx\n")
            elif op["action"] == OP_GREATER:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovg rcx, rdx\n")
                out.write("    push rcx\n")
            elif op["action"] == OP_GR_EQ:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovge rcx, rdx\n")
                out.write("    push rcx\n")
            elif op["action"] == OP_LESSER:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovl rcx, rdx\n")
                out.write("    push rcx\n")
            elif op["action"] == OP_LESS_EQ:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovle rcx, rdx\n")
                out.write("    push rcx\n")
            elif op["action"] == OP_IF:
                assert len(op) > 1, "ERROR: `if` block has no referenced `end`"
                out.write("    pop rax\n")
                out.write("    test rax, rax\n")
                out.write("    jz addr_%d\n" % op["jump_to"])
            elif op["action"] == OP_ELSE:
                out.write("    jmp addr_%d\n" % op["jump_to"])
            elif op["action"] == OP_FI:
                out.write("    jmp addr_%d\n" % op["jump_to"])
            elif op["action"] == OP_WHILE:
                pass
            elif op["action"] == OP_DO:
                assert len(op) > 1, "ERROR: `do` block has no referenced `end`"
                out.write("    pop rax\n")
                out.write("    test rax, rax\n")
                out.write("    jz addr_%d\n" % op["jump_to"])
            elif op["action"] == OP_DONE:
                out.write("    jmp addr_%d\n" % op["jump_to"])
            elif op["action"] == OP_END:
                assert False, "not implemented"
            elif op["action"] == OP_MEM_ADDR:
                out.write("    push mem\n")
            elif op["action"] == OP_MEM_STORE:
                out.write("    pop rbx\n")
                out.write("    pop rax\n")
                out.write("    mov [rax], bl\n")
            elif op["action"] == OP_MEM_LOAD:
                out.write("    pop rax\n")
                out.write("    xor rbx, rbx\n")
                out.write("    mov bl, [rax]\n")
                out.write("    push rbx\n")
            elif op["action"] == OP_SYSCALL:
                out.write("    pop rax\n")
                out.write("    pop rdi\n")
                out.write("    pop rsi\n")
                out.write("    pop rdx\n")
                out.write("    syscall\n")
            elif op["action"] == OP_EXIT:
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
        out.write("    mem: resb %d\n" % (STR_ALLOCATION_SIZE + MEM_ALLOCATION_SIZE))
        out.write("segment .data\n")
        for index, string in enumerate(str_stack):
            out.write("    str_%d: db " % index)
            for char in string:
                out.write("%d, " % char)
            out.write("\n")
        out.close()
        call_cmd()

def usage(program):
    print("-------------------------------------------")
    print("Usage: %s <SUBCOMMAND> [ARGS]" % program)
    print("SUBCOMMANDS:")
    print("    --compile  (-c) <file>       Compile the program to Assembly")
    print("    --help                       Provide usage details")
    print("    --simulate (-s) <file>       Simulate the program using Python3")
    print("-------------------------------------------")
    exit(1)

def call_cmd():
    print("BUILD:-------------------------------------")
    print("run: nasm -felf64 build/output.asm")
    subprocess.call(["nasm", "-felf64", "build/output.asm"])
    print("run: ld -o build/output build/output.o")
    subprocess.call(["ld", "-o", "build/output", "build/output.o"])
    print("run: build/output")
    print("-------------------------------------------")

if __name__ == "__main__":
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
                print("\n-------------------------------------------")
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
        print("ERROR: unknown nova subcommand `%s`" % (subcommand))
        usage(program)
