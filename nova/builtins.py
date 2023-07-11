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

