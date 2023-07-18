from nova.helpers import find_next, get_macro_or_const_name
from nova.builtins import Builtins, OperandId, TokenId
from nova.dataclasses import Symbol, FileLocation, Token, Operand, Program


# TODO implement Tokenizer class (which tokenizes a file)
# TODO implement Lexer as a class (which runs lexical analysis over tokens: generate blocks etc)

def get_next_symbol(line: str, start: int):
    token_start = find_next(line, start, lambda x : not x.isspace()) 
    if line[token_start] == "\"":
        token_end = find_next(line, token_start+1, lambda x : x == "\"")
        return Symbol(
                start = token_start, 
                end = token_end+1, 
                value = line[token_start+1:token_end], 
                string = True
                )
    else:
        token_end = find_next(line, token_start, lambda x : x.isspace())
        return Symbol(
                start = token_start, 
                end = token_end, 
                value = line[token_start:token_end], 
                string = False)


def assign_token_type(token: str, typ: str):
    if typ == "str":
        return (TokenId.STR, bytes(token, "utf-8").decode("unicode_escape"))
    elif typ == "macro":
        return (TokenId.MACRO, token)
    elif typ == "const":
        return (TokenId.CONST, token)
    elif typ == "op":
        return (TokenId.OP, token)
    else:
        try:
            return (TokenId.INT, int(token))
        except ValueError:
            assert False, "ERROR: unknown operand"


def lex_line_to_tokens(line: str):
    start = 0
    end = 0
    while start < len(line)-1:
        symbol = get_next_symbol(line, start)
        if symbol.string:
            end = symbol.end
            yield(start, assign_token_type(symbol.value, typ="str"))
        elif symbol.value == "macro":
            (name, start, end) = get_macro_or_const_name(line, start)
            if name in Builtins.BUILTIN_MACRO:
                assert False, "ERROR: attempting to override a built-in macro {} - not permitted".format(name)
            (macro_stack, start, end) = parse_macro_stack(name, line, start, end)
            Builtins.BUILTIN_MACRO[name] = macro_stack
            end = end
        elif symbol.value in Builtins.BUILTIN_MACRO:
            end = symbol.end
            yield(start, assign_token_type(symbol.value, typ="macro"))
        elif symbol.value == "const":
            (name, start, end) = get_macro_or_const_name(line, start)
            if name in Builtins.BUILTIN_CONST:
                assert False, "ERROR: attempting to override a built-in constant {} - not permitted".format(name)
            (value, start, end) = parse_const_int(line, start, end)
            Builtins.BUILTIN_CONST[name] = int(value)
        elif symbol.value in Builtins.BUILTIN_CONST:
            end = symbol.end
            yield(start, assign_token_type(line[start:end], typ="const"))
        elif symbol.value in Builtins.BUILTIN_OPS:
            end = symbol.end
            yield(start, assign_token_type(symbol.value, typ="op"))
        else:
            end = symbol.end
            yield(start, assign_token_type(symbol.value, "int"))
        start = end+1

def parse_macro_stack(name, line, start, end):
    macro_stack = []
    start = find_next(line, end+1, lambda x: not x.isspace())
    if "end" in line:
        while line[start:find_next(line, start, lambda x: x.isspace())] != "end":
            end = find_next(line, start, lambda x: x.isspace());
            if line[start:end] != name:
                macro_stack.append(line[start:end])
                start = find_next(line, end+1, lambda x: not x.isspace())
            else:
                assert False, "ERROR: {} not a valid symbol to add to a MACRO, no recursive macros".format(line[start:end])
        end = find_next(line, start, lambda x: x.isspace())
        return (macro_stack, start, end)
    else:
        assert False, "ERROR: when establishing a macro you must supply an `end` symbol - no `end` found on line"


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
        program = [Token(typ      = token_type,
                      location = FileLocation(input_file_path, line_number+1, col+1),
                      value    = token_value)
                for (line_number, line) in enumerate(file.readlines())
                for (col, (token_type, token_value)) in lex_line_to_tokens(line.split("//")[0])]
        return program

def parse_macro(macro):
    instructions = Builtins.BUILTIN_MACRO[macro]
    if macro in Builtins.BUILTIN_MACRO:
        for i in instructions:
            if i in Builtins.BUILTIN_OPS:
                yield(Builtins.BUILTIN_OPS[i], i)
            elif isinstance(int(i), int):
                yield(OperandId.PUSH_INT, int(i))
            else:
                assert False, "ERROR: `%s` not found in Builtins.BUILTIN_OPS" % i

def parse_const_int(line, start, end):
    start = find_next(line, end+1, lambda x: not x.isspace())
    end = find_next(line, start, lambda x: x.isspace())
    value = line[start:end]
    try:
        return (int(value), start, end)
    except ValueError:
        assert False, "ERROR: const value must be of type integer"

