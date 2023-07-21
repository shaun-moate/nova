from enum import Enum, auto

## TODO: Add OP_ASSERT to support testing framework - enabling us to ensure we can assert() the expected correct result
class OperandId(Enum):
    PUSH_INT  = auto()
    PUSH_STR  = auto()
    OVER      = auto()
    SWAP      = auto()
    DUP       = auto()
    DUP2      = auto()
    DROP      = auto()
    DUMP      = auto()
    SHL       = auto()
    SHR       = auto()
    BAND      = auto()
    BOR       = auto()
    PLUS      = auto()
    MINUS     = auto()
    MULT      = auto()
    EQUAL     = auto()
    NOT_EQUAL = auto()
    GREATER   = auto()
    GR_EQ     = auto()
    LESSER    = auto()
    LESS_EQ   = auto()
    IF        = auto()
    ELSE      = auto()
    FI        = auto()
    WHILE     = auto()
    DO        = auto()
    DONE      = auto()
    END       = auto()
    MEM_ADDR  = auto()
    MEM_STORE = auto()
    MEM_LOAD  = auto()
    SYSCALL   = auto()
    EXIT      = auto()

class MacroId(Enum):
    WRITE     = auto()

class ConstantId(Enum):
    CATCH     = auto()

class TokenId(Enum):
    OP        = auto()
    MACRO     = auto()
    CONST     = auto()
    INT       = auto()
    STR       = auto()

class Builtins:
    ## TODO: add `include` to support the inclusion of base libraries of operations (ie. include "nova:core")
    ## TODO: add `{` and `}` as operands to help segment blocks and improve readability
    ## TODO: add `(` and `)` as operands to help with math ordering`
    BUILTIN_OPS = {
        "int":     OperandId.PUSH_INT,
        "str":     OperandId.PUSH_STR,
        "+":       OperandId.PLUS,
        "-":       OperandId.MINUS,
        "*":       OperandId.MULT,
        "==":      OperandId.EQUAL,
        "!=":      OperandId.NOT_EQUAL,
        ">":       OperandId.GREATER,
        ">=":      OperandId.GR_EQ,
        "<":       OperandId.LESSER,
        "<=":      OperandId.LESS_EQ,
        "if":      OperandId.IF,
        "else":    OperandId.ELSE,
        "fi":      OperandId.FI,
        "while":   OperandId.WHILE,
        "do":      OperandId.DO,
        "done":    OperandId.DONE,
        "end":     OperandId.END,
        "mem":     OperandId.MEM_ADDR,
        "store8":  OperandId.MEM_STORE,
        "load8":   OperandId.MEM_LOAD,
        "syscall": OperandId.SYSCALL,
        "over":    OperandId.OVER,
        "swap":    OperandId.SWAP,
        "dup":     OperandId.DUP,
        "2dup":    OperandId.DUP2,
        "dump":    OperandId.DUMP,
        "drop":    OperandId.DROP,
        "shl":     OperandId.SHL,
        "shr":     OperandId.SHR,
        "band":    OperandId.BAND,
        "bor":     OperandId.BOR,
        "exit":    OperandId.EXIT
    }

    BUILTIN_CONST = {
        "CATCH":   (TokenId.INT, 22),
    }

    ## TODO: add MACROS to examples to improve readability -> ie. rule110.nv
    BUILTIN_MACRO = {
        "write":   [(TokenId.INT, 1), (TokenId.INT, 1), (TokenId.OP, 'syscall')],
    }


