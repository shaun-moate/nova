segment .text
dump:
    mov r9, -3689348814741910323
    sub rsp, 40
    mov BYTE [rsp+31], 10
    lea rcx, [rsp+30]
.L2:
    mov rax, rdi
    lea r8, [rsp+32]
    mul r9
    mov rax, rdi
    sub r8, rcx
    shr rdx, 3
    lea rsi, [rdx+rdx*4]
    add rsi, rsi
    sub rax, rsi
    add eax, 48
    mov BYTE [rcx], al
    mov rax, rdi
    mov rdi, rdx
    mov rdx, rcx
    sub rcx, 1
    cmp rax, 9
    ja  .L2
    lea rax, [rsp+32]
    mov edi, 1
    sub rdx, rax
    xor eax, eax
    lea rsi, [rsp+32+rdx]
    mov rdx, r8
    mov rax, 1
    syscall
    add rsp, 40
    ret
global _start
_start:
addr_0:
    push 34
addr_1:
    push 35
addr_2:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_3:
    pop rdi
    call dump
addr_4:
    push 500
addr_5:
    push 80
addr_6:
    pop rax
    pop rbx
    sub rbx, rax
    push rbx
addr_7:
    pop rdi
    call dump
addr_8:
    push 7
addr_9:
    push 6
addr_10:
    pop rax
    pop rbx
    mul rbx
    push rax
addr_11:
    pop rdi
    call dump
addr_12:
    mov rax, 60
    mov rdi, 0
    syscall