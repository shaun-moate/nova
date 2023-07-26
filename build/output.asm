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
    push mem
addr_1:
    push 0
addr_2:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_3:
    push 97
addr_4:
    pop rbx
    pop rax
    mov [rax], bl
addr_5:
    push mem
addr_6:
    push 1
addr_7:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_8:
    push 98
addr_9:
    pop rbx
    pop rax
    mov [rax], bl
addr_10:
    push mem
addr_11:
    push 2
addr_12:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_13:
    push 99
addr_14:
    pop rbx
    pop rax
    mov [rax], bl
addr_15:
    push 3
addr_16:
    push mem
addr_17:
    push 1
addr_18:
    push 1
addr_19:
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
addr_20:
    mov rax, 60
    mov rdi, 0
    syscall
segment .bss
    mem: resb 138000
segment .data
