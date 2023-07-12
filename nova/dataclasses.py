from dataclasses import dataclass, field
from typing import List, Union

from nova.builtins import TokenId, OperandId

@dataclass
class FileLocation:
    file_path: str
    row:       int
    col:       int

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

