from nova.helpers import *

## uncons
def test_check_uncons_works_as_expected():
    argv = ['file', '-f', 'tests/example.nv']
    program, result = uncons(argv)
    assert program == 'file' and result == ['-f', 'tests/example.nv']

def test_check_uncons_gets_subcommand():
    argv = ['file', '-f', 'tests/example.nv']
    program, result = uncons(argv)
    subcommand, argv = uncons(result)
    assert program == 'file' and subcommand == '-f'

def test_check_uncons_gets_file_path():
    argv = ['file', '-f', 'tests/example.nv']
    program, argv = uncons(argv)
    subcommand, argv = uncons(argv)
    file_path, argv = uncons(argv)
    assert program == 'file' and subcommand == '-f' and file_path == 'tests/example.nv'

def test_check_uncons_when_blank_args():
    argv = ['file']
    program, argv = uncons(argv)
    assert program == 'file' and argv == []

## find_next
def test_check_find_next_works_as_expected():
    line = '  34 35 + dump'
    start = find_next(line, 0, lambda x: not x.isspace())
    assert start == 2
    
def test_check_find_next_end_of_token():
    line = '  34 35 + dump'
    start = find_next(line, 0, lambda x: not x.isspace())
    end = find_next(line, start, lambda x: x.isspace())
    assert end == 4

def test_check_find_get_first_token():
    line = '  34 35 + dump'
    start = find_next(line, 0, lambda x: not x.isspace())
    end = find_next(line, start, lambda x: x.isspace())
    token = line[start:end]
    assert token == '34'

## unnest_program


'''
from nova.dataclasses import Program

def unnest_program(program: Program):
    result = []
    for i in range(len(program.operands)):
        if type(program.operands[i]) is list:
            for j in range(len(program.operands[i])):
                result.append(program.operands[i][j])
        else:
            result.append(program.operands[i])
    program.operands = result
    return program
'''

