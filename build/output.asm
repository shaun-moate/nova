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
    push 13
    push 13
    pop rax
    pop rbx
    add rax, rbx
    push rax
    push 26
    mov rcx, 0
    mov rdx, 1
    pop rax
    pop rbx
    cmp rax, rbx
    cmove rcx, rdx
    push rcx
    pop rdi
    call dump
    push 3
    push 23
    pop rax
    pop rbx
    imul rbx
    push rax
    pop rdi
    call dump
    push 10
    push 10
    pop rax
    pop rbx
    imul rbx
    push rax
    pop rdi
    call dump
    push 0
    push 9
    pop rax
    pop rbx
    imul rbx
    push rax
    pop rdi
    call dump
    push -1
    push 9
    pop rax
    pop rbx
    imul rbx
    push rax
    pop rdi
    call dump
    mov rax, 60
    mov rdi, 0
    syscall