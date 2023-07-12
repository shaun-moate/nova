from nova.config import Config
from nova.builtins import OperandId

def simulate_program(program):
    stack = []
    mem = bytearray(Config.MEM_ALLOCATION_SIZE + Config.STR_ALLOCATION_SIZE)
    str_addr_start = 0
    ip = 0
    while ip < len(program.operands):
        assert len(OperandId) == 33, "Exhaustive list of operands in simulate_program()"
        op = program.operands[ip]
        if op.action == OperandId.PUSH_INT:
            stack.append(op.value)
            ip += 1
        elif op.action == OperandId.PUSH_STR:
            str_bytes = bytes(op.value, "utf-8")
            str_length = len(str_bytes)
            if op.mem_addr == -1:
                op.mem_addr = str_addr_start
                for i in reversed(range(str_length)):
                    mem[str_addr_start+i] = str_bytes[i]
                str_addr_start += str_length
                assert str_addr_start <= Config.STR_ALLOCATION_SIZE, "ERROR: String buffer overflow"
            stack.append(str_length)
            stack.append(op.mem_addr)
            ip += 1
        elif op.action == OperandId.OVER:
            x = stack.pop()
            y = stack.pop()
            stack.append(y)
            stack.append(x)
            stack.append(y)
            ip += 1
        elif op.action == OperandId.SWAP:
            x = stack.pop()
            y = stack.pop()
            stack.append(x)
            stack.append(y)
            ip += 1
        elif op.action == OperandId.DROP:
            stack.pop()
            ip += 1
        elif op.action == OperandId.DUMP:
            x = stack.pop()
            print(x)
            ip += 1
        elif op.action == OperandId.DUP:
            x = stack.pop()
            stack.append(x)
            stack.append(x)
            ip += 1
        elif op.action == OperandId.DUP2:
            x = stack.pop()
            y = stack.pop()
            stack.append(y)
            stack.append(x)
            stack.append(y)
            stack.append(x)
            ip += 1
        elif op.action == OperandId.SHL:
            x = stack.pop()
            y = stack.pop()
            stack.append(y << x)
            ip += 1
        elif op.action == OperandId.SHR:
            x = stack.pop()
            y = stack.pop()
            stack.append(y >> x)
            ip += 1
        elif op.action == OperandId.BAND:
            x = stack.pop()
            y = stack.pop()
            stack.append(y & x)
            ip += 1
        elif op.action == OperandId.BOR:
            x = stack.pop()
            y = stack.pop()
            stack.append(y | x)
            ip += 1
        elif op.action == OperandId.PLUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
            ip += 1
        elif op.action == OperandId.MINUS:
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
            ip += 1
        elif op.action == OperandId.MULT:
            x = stack.pop()
            y = stack.pop()
            stack.append(y * x)
            ip += 1
        elif op.action == OperandId.EQUAL:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y == x))
            ip += 1
        elif op.action == OperandId.NOT_EQUAL:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y != x))
            ip += 1
        elif op.action == OperandId.GREATER:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y > x))
            ip += 1
        elif op.action == OperandId.GR_EQ:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y >= x))
            ip += 1
        elif op.action == OperandId.LESSER:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y < x))
            ip += 1
        elif op.action == OperandId.LESS_EQ:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y <= x))
            ip += 1
        elif op.action == OperandId.IF:
            if stack.pop() == 0:
                ip = op.jump_to
            else:
                ip += 1
        elif op.action == OperandId.ELSE:
            ip = op.jump_to
        elif op.action == OperandId.FI:
            ip = op.jump_to
        elif op.action == OperandId.WHILE:
            ip += 1
        elif op.action == OperandId.DO:
            if stack.pop() == 0:
                ip = op.jump_to
            else:
                ip += 1
        elif op.action == OperandId.DONE:
            ip = op.jump_to
            ip += 1
        elif op.action == OperandId.END:
            ip += 1
        elif op.action == OperandId.MEM_ADDR:
            stack.append(Config.STR_ALLOCATION_SIZE)
            ip += 1
        elif op.action == OperandId.MEM_STORE:
            byte = stack.pop()
            addr = stack.pop()
            mem[addr] = byte & 0xFF
            ip += 1
        elif op.action == OperandId.MEM_LOAD:
            addr = stack.pop()
            byte = mem[addr]
            stack.append(byte)
            ip += 1
        elif op.action == OperandId.SYSCALL:
            syscall_num = stack.pop()
            arg1 = stack.pop()
            arg2 = stack.pop()
            arg3 = stack.pop()
            if syscall_num == 1:
                print(mem[arg2:arg2+arg3].decode("utf-8"), end="")
            ip += 1
        elif op.action == OperandId.EXIT:
            x = stack.pop()
            exit(x)
            ip += 1
        else:
            assert False, "OperandIderands is unreachable"

