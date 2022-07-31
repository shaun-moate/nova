#!/usr/bin/env python3

import bin.config as cfg

def push(value):
    return (cfg.OP_PUSH, value)

def plus():
    return (cfg.OP_PLUS, )

def minus():
    return (cfg.OP_MINUS, )

def multiply():
    return (cfg.OP_MULT, )

def equal():
    return (cfg.OP_EQUAL, )

def not_equal():
    return (cfg.OP_NOT_EQUAL, )

def greater_than():
    return (cfg.OP_GREATER, )

def greater_than_or_equal():
    return (cfg.OP_GR_EQ, )

def less_than():
    return (cfg.OP_LESSER, )

def less_than_or_equal():
    return (cfg.OP_LESS_EQ, )

def iff():
    return (cfg.OP_IF, )

def elsef():
    return (cfg.OP_ELSE, )

def end():
    return (cfg.OP_END, )

def dump():
    return (cfg.OP_DUMP, )

def parse_token_as_op(token):
    (file_path, row, col, word) = token
    assert cfg.OP_COUNT == 14, "Exhaustive list of operands in parse_token_as_op()"
    if word == "+":
        return plus()
    elif word == "-":
        return minus()
    elif word == "*":
        return multiply()
    elif word == "==":
        return equal()
    elif word == "!=":
        return not_equal()
    elif word == ">":
        return greater_than()
    elif word == ">=":
        return greater_than_or_equal()
    elif word == "<":
        return less_than()
    elif word == "<=":
        return less_than_or_equal()
    elif word == "if":
        return iff()
    elif word == "else":
        return elsef()
    elif word == "end":
        return end()
    elif word == "print":
        return dump()
    elif "." not in word:
        try:
            return push(int(word))
        except ValueError as err:
            print("%s:%d:%d:   %s " % (file_path, row, col, err))
            exit(1)
    else:
        assert False, "Operand is unreachable"

def parse_program_from_file(input_file_path):
    with open(input_file_path, "r") as file:
        return generate_blocks(
                    [parse_token_as_op(token) for token in parse_tokens_from_file(input_file_path)]
                )

def parse_tokens_from_file(input_file_path):
    with open(input_file_path, "r") as file:
        return [(input_file_path, row+1, col+1, token)
                for (row, line) in enumerate(file.readlines())
                for (col, token) in parse_line(line)]

def parse_line(line):
    start = find_next(line, 0, lambda x: not x.isspace())
    while start < len(line):
        end = find_next(line, start, lambda x: x.isspace())
        yield(start, line[start:end])
        start = find_next(line, end+1, lambda x: not x.isspace())

def find_next(line, start, predicate):
    while start < len(line) and not predicate(line[start]):
        start += 1
    return start

def generate_blocks(program):
    block = []
    for ip in range(len(program)):
        assert cfg.OP_COUNT == 14, "Exhaustive list of operands in generate_blocks() -> Note: only operands that generate a block need to be included."
        if program[ip][0] == cfg.OP_IF:
            block.append(ip)
        if program[ip][0] == cfg.OP_ELSE:
            ref = block.pop()
            assert program[ref][0] == cfg.OP_IF, "ERROR: 'else' can only be used in 'if' blocks"
            program[ref] = (cfg.OP_IF,  ip+1)
            block.append(ip)
        if program[ip][0] == cfg.OP_END:
            ref = block.pop()
            program[ref] = (program[ref][0],  ip)
    return program
