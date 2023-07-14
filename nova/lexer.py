from nova.helpers import find_next
from nova.builtins import Builtins, OperandId, TokenId
from nova.dataclasses import FileLocation, Token, Operand, Program

def parse_program_from_file(input_file_path: str) -> Program:
    with open(input_file_path, "r"):
        return generate_blocks(
                    Program(operands = [parse_token_as_op(token) 
                                        for token in parse_tokens_from_file(input_file_path)])
                )

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


def generate_blocks(program: Program) -> Program:
    block = []
    program = unnest_program(program)
    for ip in range(len(program.operands)):
        assert len(OperandId) == 33, "Exhaustive list of operands"
        if program.operands[ip].action == OperandId.IF:
            block.append(ip)
        if program.operands[ip].action == OperandId.ELSE:
            ref = block.pop()
            assert program.operands[ref].action == OperandId.IF, "ERROR: `else` can only be used in `if` blocks"
            program.operands[ref].action = OperandId.IF
            program.operands[ref].jump_to = ip+1
            block.append(ip)
        if program.operands[ip].action == OperandId.FI:
            ref = block.pop()
            assert program.operands[ref].action == OperandId.IF or program.operands[ref].action == OperandId.ELSE, "ERROR: `fi` is expected to end the blocks for `if` or `else` only"
            program.operands[ip].jump_to = ip+1
            program.operands[ref].jump_to = ip
        if program.operands[ip].action == OperandId.WHILE:
            block.append(ip)
        if program.operands[ip].action == OperandId.DO:
            ref = block.pop()
            assert program.operands[ref].action == OperandId.WHILE, "ERROR: `do` can only be used in `while` blocks"
            program.operands[ip].jump_to = ref
            block.append(ip)
        if program.operands[ip].action == OperandId.DONE:
            ref = block.pop()
            program.operands[ip].jump_to = program.operands[ref].jump_to
            program.operands[ref].action = OperandId.DO
            program.operands[ref].jump_to = ip+1
        if program.operands[ip].action == OperandId.END:
           pass
    return program

def parse_token_as_op(token: Token):
    location = token.location
    assert len(TokenId) == 5, "Exhaustive list of operands in parse_word()"
    if token.typ == TokenId.OP:
        if token.value in Builtins.BUILTIN_OPS:
            return Operand(action   = Builtins.BUILTIN_OPS[token.value],
                           jump_to  = -1,
                           mem_addr = -1,
                           location = location,
                           value    = token.value)
        else:
            print("%s:%d:%d: ERROR: unknown operand `%s` found".format(token.location, (token.value, )))
            exit(1)
    elif token.typ == TokenId.MACRO:
        return [Operand(action   = action,
                        jump_to  = -1,
                        mem_addr = -1,
                        location = token.location,
                        value    = value)
                for (action, value) in parse_macro(token.value)]
    elif token.typ == TokenId.CONST:
        if token.value in Builtins.BUILTIN_CONST:
            return Operand(action   = OperandId.PUSH_INT,
                           jump_to  = -1,
                           mem_addr = -1,
                           location = token.location,
                           value    = Builtins.BUILTIN_CONST[token.value])
    elif token.typ == TokenId.INT:
        return Operand(action   = OperandId.PUSH_INT,
                       jump_to  = -1,
                       mem_addr = -1,
                       location = token.location,
                       value    = token.value)
    elif token.typ == TokenId.STR:
        return Operand(action   = OperandId.PUSH_STR,
                       jump_to  = -1,
                       mem_addr = -1,
                       location = token.location,
                       value    = token.value)
    else:
        assert False, "TokenId type is unreachable is unreachable"

def parse_tokens_from_file(input_file_path: str):
    with open(input_file_path, "r") as file:
        return [Token(typ      = token_type,
                      location = FileLocation(input_file_path, row+1, col+1),
                      value    = token_value)
                for (row, line) in enumerate(file.readlines())
                for (col, (token_type, token_value)) in parse_line(line.split("//")[0])]

def parse_macro(macro):
    instructions = Builtins.BUILTIN_MACRO[macro]
    if macro in Builtins.BUILTIN_MACRO:
        for i in instructions:
            if parse_word(i)[0] == TokenId.OP:
                if i in Builtins.BUILTIN_OPS:
                    yield(Builtins.BUILTIN_OPS[i], i)
                else:
                    assert False, "ERROR: `%s` not found in Builtins.BUILTIN_OPS" % i
            elif parse_word(i)[0] == TokenId.INT:
                yield(OperandId.PUSH_INT, int(i))

def parse_line(line: str):
    start = find_next(line, 0, lambda x : not x.isspace())
    while start < len(line):
        if line[start] == "\"":
            end = find_next(line, start+1, lambda x : x == "\"")
            yield(start, parse_word(line[start+1:end], typ="str"))
        elif line[start:find_next(line, start, lambda x : x.isspace())] == "macro":
            (name, start, end) = parse_name(line, start)
            if name in Builtins.BUILTIN_MACRO:
                print("ERROR: attempting to override a built-in macro `%s` - not permitted" % name)
                exit(1)
            (macro_stack, start, end) = parse_macro_stack(line, start, end)
            Builtins.BUILTIN_MACRO[name] = macro_stack
            start = find_next(line, end+1, lambda x: not x.isspace())
        elif line[start:find_next(line, start, lambda x: x.isspace())] in Builtins.BUILTIN_MACRO:
            end = find_next(line, start, lambda x: x.isspace())
            yield(start, parse_word(line[start:end], typ="macro"))
        elif line[start:find_next(line, start, lambda x: x.isspace())] == "const":
            (name, start, end) = parse_name(line, start)
            if name in Builtins.BUILTIN_CONST:
                print("ERROR: attempting to override a built-in constant `%s` - not permitted" % name)
                exit(1)
            (value, start, end) = parse_const_int(line, start, end)
            Builtins.BUILTIN_CONST[name] = int(value)
        elif line[start:find_next(line, start, lambda x: x.isspace())] in Builtins.BUILTIN_CONST:
            end = find_next(line, start, lambda x: x.isspace())
            yield(start, parse_word(line[start:end], typ="const"))
        else:
            end = find_next(line, start, lambda x: x.isspace())
            yield(start, parse_word(line[start:end]))
        start = find_next(line, end+1, lambda x: not x.isspace())

def parse_name(line: str, start: int):
    skip_end = find_next(line, start, lambda x: x.isspace())
    start_next = find_next(line, skip_end+1, lambda x: not x.isspace())
    end_next = find_next(line, start_next, lambda x: x.isspace())
    return (line[start_next:end_next], start_next, end_next)

def parse_macro_stack(line, start, end):
    macro_stack = []
    start = find_next(line, end+1, lambda x: not x.isspace())
    while line[start:find_next(line, start, lambda x: x.isspace())] != "end":
        end = find_next(line, start, lambda x: x.isspace())
        assert parse_word(line[start:end])[0] == TokenId.OP or parse_word(line[start:end])[0] == TokenId.INT, "ERROR: macro op value must be of type operation or integer"
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

def parse_word(token: str, typ=None):
    assert len(TokenId) == 5, "Exhaustive list of operands in parse_word()"
    if typ == "str":
        return (TokenId.STR, bytes(token, "utf-8").decode("unicode_escape"))
    elif typ == "macro":
        return (TokenId.MACRO, token)
    elif typ == "const":
        return (TokenId.CONST, token)
    else:
        try:
            return (TokenId.INT, int(token))
        except ValueError:
            return (TokenId.OP, token)

