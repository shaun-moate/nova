from nova.helpers import find_next
from nova.builtins import Builtins, OperandId, TokenId
from nova.dataclasses import Symbol, FileLocation, Token, Operand, Program


# TODO implement Lexer as a class ) - is basically a tokenizer, but it usually attaches extra context to the tokens
# Lexer will define scopes for those tokens (variables/functions)

# TODO add 'import' functionality to create a standard library (initialising macros, consts from library)

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
            yield(symbol.start, assign_token_type(symbol.value, typ="str"))
        elif symbol.value == "macro":
            name = get_next_symbol(line, symbol.end)
            if name.value in Builtins.BUILTIN_MACRO:
                assert False, "ERROR: attempting to override a built-in macro {} - not permitted".format(name.value)
            end = store_macro(line, name.value, name.end)
        elif symbol.value in Builtins.BUILTIN_MACRO:
            end = symbol.end
            yield(symbol.start, assign_token_type(symbol.value, typ="macro"))
        elif symbol.value == "const":
            name = get_next_symbol(line, symbol.end)
            if name.value in Builtins.BUILTIN_CONST:
                assert False, "ERROR: attempting to override a built-in constant {} - not permitted".format(name.value)
            end = store_const(line, name.value, name.end)
        elif symbol.value in Builtins.BUILTIN_CONST:
            end = symbol.end
            yield(symbol.start, assign_token_type(line[start:end], typ="const"))
        elif symbol.value in Builtins.BUILTIN_OPS:
            end = symbol.end
            yield(symbol.start, assign_token_type(symbol.value, typ="op"))
        else:
            end = symbol.end
            yield(symbol.start, assign_token_type(symbol.value, "int"))
        start = end+1

def store_const(line, name, start):
    integer = get_next_symbol(line, start)
    try:
        Builtins.BUILTIN_CONST[name] = assign_token_type(integer.value, "int")
        return integer.end
    except ValueError:
        assert False, "ERROR: const value must be of type integer"

def store_macro(line, name, start):
    macro_stack = []
    if "end" in line:
        symbol = get_next_symbol(line, start)
        while symbol.value != "end":
            if symbol.value != name:
                if symbol.string:
                    macro_stack.append(assign_token_type(symbol.value, "str"))
                elif symbol.value in Builtins.BUILTIN_OPS:
                    macro_stack.append(assign_token_type(symbol.value, "op"))
                else:
                    macro_stack.append(assign_token_type(symbol.value, "int"))
                symbol = get_next_symbol(line, symbol.end)
            else:
                assert False, "ERROR: {} not a valid symbol to add to a MACRO, no recursive macros".format(symbol.value)
        Builtins.BUILTIN_MACRO[name] = macro_stack
        return symbol.end
    else:
        assert False, "ERROR: when establishing a macro you must supply an `end` symbol - no `end` found on line"

# TODO Add typing to functions including expected return types
def lex_macro_from_builtins(macro):
    if macro in Builtins.BUILTIN_MACRO:
        instructions = Builtins.BUILTIN_MACRO[macro]
        for token in instructions:
            if token[1] in Builtins.BUILTIN_OPS:
                yield(Builtins.BUILTIN_OPS[token[1]], token[1])
            elif isinstance(int(token[1]), int):
                yield(OperandId.PUSH_INT, int(token[1]))
            else:
                assert False, "ERROR: `%s` not found in Builtins.BUILTIN_OPS" % token[1]

def lex_tokens_from_file(input_file_path: str):
    with open(input_file_path, "r") as file:
        program = [Token(typ      = token_type,
                      location = FileLocation(input_file_path, line_number+1, col+1),
                      value    = token_value)
                for (line_number, line) in enumerate(file.readlines())
                for (col, (token_type, token_value)) in lex_line_to_tokens(line.split("//")[0])]
        return program


def parse_program_from_file(input_file_path: str) -> Program:
    with open(input_file_path, "r"):
        return generate_blocks(
                    Program(operands = [parse_token_as_op(token) 
                                        for token in lex_tokens_from_file(input_file_path)])
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
                for (action, value) in lex_macro_from_builtins(token.value)]
    elif token.typ == TokenId.CONST:
        if token.value in Builtins.BUILTIN_CONST:
            return Operand(action   = OperandId.PUSH_INT,
                           jump_to  = -1,
                           mem_addr = -1,
                           location = token.location,
                           value    = Builtins.BUILTIN_CONST[token.value][1])
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


