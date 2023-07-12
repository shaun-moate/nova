from nova.dataclasses import Program

def uncons(xs):
    return (xs[0], xs[1:])

def find_next(line: str, start: int, predicate) -> int:
    while start < len(line) and not predicate(line[start]):
        start += 1
    return start

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


