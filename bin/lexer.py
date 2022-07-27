#!/usr/bin/env python3

import bin.config as cfg

def push(value):
    return (cfg.OP_PUSH, value)

def plus():
    return (cfg.OP_PLUS, )

def minus():
    return (cfg.OP_MINUS, )

def equal():
    return (cfg.OP_EQUAL, )

def dump():
    return (cfg.OP_DUMP, )

def parse_token_as_op(token):
    (file_path, row, col, word) = token
    assert cfg.OP_COUNT == 5, "Exhaustive list of operands in emulate_program()"
    if word == "+":
        return plus()
    elif word == "-":
        return minus()
    elif word == "=":
        return equal()
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
        return[parse_token_as_op(token) for token in parse_tokens_from_file(input_file_path)]

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
