#!/usr/bin/env python3

import bin.config as cfg

def push(value):
    return (cfg.OP_PUSH, value)

def plus():
    return (cfg.OP_PLUS, )

def minus():
    return (cfg.OP_MINUS, )

def dump():
    return (cfg.OP_DUMP, )

def parse_program_from_file(input_file_path):
    with open(input_file_path, "r") as f:
        return [parse_token_as_op(token) for token in f.read().split()]

def parse_token_as_op(token):
    assert cfg.OP_COUNT == 4, "Exhaustive list of operands in emulate_program()"
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
