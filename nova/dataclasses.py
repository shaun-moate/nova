from dataclasses import dataclass, field
from typing import List, Union

from nova.builtins import TokenId, OperandId

# TODO look into using attrs instead of dataclass https://www.youtube.com/watch?v=1S2h11XronA&ab_channel=mCoding
@dataclass
class Word:
    start:     int
    end:       int
    value:     str
    string:    bool

@dataclass
class FileLocation:
    file_path: str
    row:       int
    col:       int

@dataclass
class RawToken:
    location:       FileLocation
    string_literal: bool
    value:          str

@dataclass
class Token:
    typ:       TokenId
    location:  FileLocation
    value:     Union[int, str, None]

@dataclass
class Operand:
    action:    OperandId
    jump_to:   int
    mem_addr:  int
    location:  FileLocation
    value:     int | str | None

    def __getitem__(self, index):
        return self[index]

    def __len__(self):
        return len(self)

@dataclass
class Program:
    operands: List[Operand] = field(default_factory=list)
    def __len__(self):
        return len(self)

