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
    mov rax, 1
    mov rdi, 1
    mov rsi, mem
    pop rdx
    syscall
addr_17:
    push mem
addr_18:
    push 0
addr_19:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_20:
    pop rax
    push rax
    push rax
addr_21:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_22:
    push 1
addr_23:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_24:
    pop rbx
    pop rax
    mov [rax], bl
addr_25:
    push mem
addr_26:
    push 1
addr_27:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_28:
    pop rax
    push rax
    push rax
addr_29:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_30:
    push 1
addr_31:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_32:
    pop rbx
    pop rax
    mov [rax], bl
addr_33:
    push mem
addr_34:
    push 2
addr_35:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_36:
    pop rax
    push rax
    push rax
addr_37:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_38:
    push 1
addr_39:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_40:
    pop rbx
    pop rax
    mov [rax], bl
addr_41:
    push 3
addr_42:
    mov rax, 1
    mov rdi, 1
    mov rsi, mem
    pop rdx
    syscall
addr_43:
    mov rax, 60
    mov rdi, 0
    syscall
segment .bss
mem: resb 69000
