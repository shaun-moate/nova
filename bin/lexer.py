#!/usr/bin/env python3

import bin.config as cfg

def parse_token_as_op(token):
    (file_path, row, col, word) = token
    location = (file_path, row+1, col+1, word)
    assert cfg.OP_COUNT == 23, "Exhaustive list of operands in parse_token_as_op()"
    if word == "+":
        return {'action': cfg.OP_PLUS, 'location': location}
    elif word == "-":
        return {'action': cfg.OP_MINUS, 'location': location}
    elif word == "*":
        return {'action': cfg.OP_MULT, 'location': location}
    elif word == "==":
        return {'action': cfg.OP_EQUAL, 'location': location}
    elif word == "!=":
        return {'action': cfg.OP_NOT_EQUAL, 'location': location}
    elif word == ">":
        return {'action': cfg.OP_GREATER, 'location': location}
    elif word == ">=":
        return {'action': cfg.OP_GR_EQ, 'location': location}
    elif word == "<":
        return {'action': cfg.OP_LESSER, 'location': location}
    elif word == "<=":
        return {'action': cfg.OP_LESS_EQ, 'location': location}
    elif word == "if":
        return {'action': cfg.OP_IF, 'location': location, 'jump_to': 0}
    elif word == "else":
        return {'action': cfg.OP_ELSE, 'location': location, 'jump_to': 0}
    elif word == "end":
        return {'action': cfg.OP_END, 'location': location, 'jump_to': 0}
    elif word == "while":
        return {'action': cfg.OP_WHILE, 'location': location, 'jump_to': 0}
    elif word == "do":
        return {'action': cfg.OP_DO, 'location': location, 'jump_to': 0}
    elif word == "dup":
        return {'action': cfg.OP_DUPLICATE, 'location': location}
    elif word == "mem":
        return {'action': cfg.OP_MEM_ADDR, 'location': location}
    elif word == "store8":
        return {'action': cfg.OP_MEM_STORE, 'location': location}
    elif word == "load8":
        return {'action': cfg.OP_MEM_LOAD, 'location': location}
    elif word == "print":
        return {'action': cfg.OP_MEM_PRINT, 'location': location}
    elif word == "dump":
        return {'action': cfg.OP_DUMP, 'location': location}
    elif word == "exit":
        return {'action': cfg.OP_EXIT, 'location': location}
    elif word == "drop":
        return {'action': cfg.OP_DROP, 'location': location}
    elif "." not in word:
        try:
            return {'action': cfg.OP_PUSH, 'location': location, 'value': int(word)}
        except ValueError as err:
            print("%s:%d:%d:   %s " % location)
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
                for (col, token) in parse_line(line.split("##")[0])]

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
        assert cfg.OP_COUNT == 23, "Exhaustive list of operands in generate_blocks() -> Note: only operands that generate a block need to be included."
        if program[ip]['action'] == cfg.OP_IF:
            block.append(ip)
        if program[ip]['action'] == cfg.OP_ELSE:
            ref = block.pop()
            assert program[ref]['action'] == cfg.OP_IF, "ERROR: 'else' can only be used in 'if' blocks"
            program[ref] = {'action': cfg.OP_IF, 'jump_to': ip+1}
            block.append(ip)
        if program[ip]['action'] == cfg.OP_DO:
            block.append(ip)
        if program[ip]['action'] == cfg.OP_WHILE:
            ref = block.pop()
            assert program[ref]['action'] == cfg.OP_DO, "ERROR: 'do' can only be used in 'while' blocks"
            program[ip] = {'action': cfg.OP_WHILE, 'jump_to': ref}
            block.append(ip)
        if program[ip]['action'] == cfg.OP_END:
            ref = block.pop()
            if program[ref]['action'] == cfg.OP_IF or program[ref]['action'] == cfg.OP_ELSE:
                program[ip] = {'action': cfg.OP_END, 'jump_to': ip+1}
                program[ref] = {'action': program[ref]['action'], 'jump_to': ip}
            elif program[ref]['action'] == cfg.OP_WHILE:
                program[ip] = {'action': cfg.OP_END, 'jump_to': program[ref]['jump_to']}
                program[ref] = {'action': cfg.OP_WHILE, 'jump_to': ip+1}
    return program
