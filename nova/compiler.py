from nova.config import Config
from nova.helpers import call_cmd
from nova.builtins import OperandId

def compile_program(program):
    str_stack = []
    with open("build/output.asm", "w") as out:
        out.write("segment .text\n")
        out.write("dump:\n")
        out.write("    mov r9, -3689348814741910323\n")
        out.write("    sub rsp, 40\n")
        out.write("    mov BYTE [rsp+31], 10\n")
        out.write("    lea rcx, [rsp+30]\n")
        out.write(".L2:\n")
        out.write("    mov rax, rdi\n")
        out.write("    lea r8, [rsp+32]\n")
        out.write("    mul r9\n")
        out.write("    mov rax, rdi\n")
        out.write("    sub r8, rcx\n")
        out.write("    shr rdx, 3\n")
        out.write("    lea rsi, [rdx+rdx*4]\n")
        out.write("    add rsi, rsi\n")
        out.write("    sub rax, rsi\n")
        out.write("    add eax, 48\n")
        out.write("    mov BYTE [rcx], al\n")
        out.write("    mov rax, rdi\n")
        out.write("    mov rdi, rdx\n")
        out.write("    mov rdx, rcx\n")
        out.write("    sub rcx, 1\n")
        out.write("    cmp rax, 9\n")
        out.write("    ja  .L2\n")
        out.write("    lea rax, [rsp+32]\n")
        out.write("    mov edi, 1\n")
        out.write("    sub rdx, rax\n")
        out.write("    xor eax, eax\n")
        out.write("    lea rsi, [rsp+32+rdx]\n")
        out.write("    mov rdx, r8\n")
        out.write("    mov rax, 1\n")
        out.write("    syscall\n")
        out.write("    add rsp, 40\n")
        out.write("    ret\n")

        out.write("global _start\n_start:\n")
        for ip in range(len(program.operands)):
            assert len(OperandId) == 33, "Exhaustive list of operands in compile_program()"
            op = program.operands[ip]
            out.write("addr_%d:\n" % ip)
            if op.action == OperandId.PUSH_INT:
                out.write("    push %d\n" % int(op.value))
            elif op.action == OperandId.PUSH_STR:
                str_bytes = bytes(op.value, "utf-8")
                out.write("    mov rax, %d\n" % len(bytes(op.value, "utf-8")))
                out.write("    push rax\n")
                out.write("    push str_%d\n" % len(str_stack))
                str_stack.append(str_bytes)
            elif op.action == OperandId.OVER:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    push rbx\n")
                out.write("    push rax\n")
                out.write("    push rbx\n")
            elif op.action == OperandId.SWAP:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    push rax\n")
                out.write("    push rbx\n")
            elif op.action == OperandId.DROP:
                out.write("    pop rax\n")
            elif op.action == OperandId.DUMP:
                out.write("    pop rdi\n")
                out.write("    call dump\n")
            elif op.action == OperandId.DUP:
                out.write("    pop rax\n")
                out.write("    push rax\n")
                out.write("    push rax\n")
            elif op.action == OperandId.DUP2:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    push rbx\n")
                out.write("    push rax\n")
                out.write("    push rbx\n")
                out.write("    push rax\n")
            elif op.action == OperandId.SHL:
                out.write("    pop rcx\n")
                out.write("    pop rax\n")
                out.write("    shl rax, cl\n")
                out.write("    push rax\n")
            elif op.action == OperandId.SHR:
                out.write("    pop rcx\n")
                out.write("    pop rax\n")
                out.write("    shr rax, cl\n")
                out.write("    push rax\n")
            elif op.action == OperandId.BAND:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    and rax, rbx\n")
                out.write("    push rax\n")
            elif op.action == OperandId.BOR:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    or rax, rbx\n")
                out.write("    push rax\n")
            elif op.action == OperandId.PLUS:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    add rax, rbx\n")
                out.write("    push rax\n")
            elif op.action == OperandId.MINUS:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    sub rbx, rax\n")
                out.write("    push rbx\n")
            elif op.action == OperandId.MULT:
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    mul rbx\n")
                out.write("    push rax\n")
            elif op.action == OperandId.EQUAL:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rax, rbx\n")
                out.write("    cmove rcx, rdx\n")
                out.write("    push rcx\n")
            elif op.action == OperandId.NOT_EQUAL:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rax, rbx\n")
                out.write("    cmovne rcx, rdx\n")
                out.write("    push rcx\n")
            elif op.action == OperandId.GREATER:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovg rcx, rdx\n")
                out.write("    push rcx\n")
            elif op.action == OperandId.GR_EQ:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovge rcx, rdx\n")
                out.write("    push rcx\n")
            elif op.action == OperandId.LESSER:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovl rcx, rdx\n")
                out.write("    push rcx\n")
            elif op.action == OperandId.LESS_EQ:
                out.write("    mov rcx, 0\n")
                out.write("    mov rdx, 1\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    cmp rbx, rax\n")
                out.write("    cmovle rcx, rdx\n")
                out.write("    push rcx\n")
            elif op.action == OperandId.IF:
                out.write("    pop rax\n")
                out.write("    test rax, rax\n")
                out.write("    jz addr_%d\n" % op.jump_to)
            elif op.action == OperandId.ELSE:
                out.write("    jmp addr_%d\n" % op.jump_to)
            elif op.action == OperandId.FI:
                out.write("    jmp addr_%d\n" % op.jump_to)
            elif op.action == OperandId.WHILE:
                pass
            elif op.action == OperandId.DO:
                out.write("    pop rax\n")
                out.write("    test rax, rax\n")
                out.write("    jz addr_%d\n" % op.jump_to)
            elif op.action == OperandId.DONE:
                out.write("    jmp addr_%d\n" % op.jump_to)
            elif op.action == OperandId.END:
                assert False, "not implemented"
            elif op.action == OperandId.MEM_ADDR:
                out.write("    push mem\n")
            elif op.action == OperandId.MEM_STORE:
                out.write("    pop rbx\n")
                out.write("    pop rax\n")
                out.write("    mov [rax], bl\n")
            elif op.action == OperandId.MEM_LOAD:
                out.write("    pop rax\n")
                out.write("    xor rbx, rbx\n")
                out.write("    mov bl, [rax]\n")
                out.write("    push rbx\n")
            elif op.action == OperandId.SYSCALL:
                out.write("    pop rax\n")
                out.write("    pop rdi\n")
                out.write("    pop rsi\n")
                out.write("    pop rdx\n")
                out.write("    syscall\n")
            elif op.action == OperandId.EXIT:
                out.write("    mov rax, 60\n")
                out.write("    pop rdi\n")
                out.write("    syscall\n")
            else:
                assert False, "Operands is unreachable"
        out.write("addr_%d:\n" % len(program.operands))
        out.write("    mov rax, 60\n")
        out.write("    mov rdi, 0\n")
        out.write("    syscall\n")
        out.write("segment .bss\n")
        out.write("    mem: resb %d\n" % (Config.STR_ALLOCATION_SIZE + Config.MEM_ALLOCATION_SIZE))
        out.write("segment .data\n")
        for index, string in enumerate(str_stack):
            out.write("    str_%d: db " % index)
            for char in string:
                out.write("%d, " % char)
            out.write("\n")
        out.close()
        call_cmd()
