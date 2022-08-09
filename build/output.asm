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
    push 72
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
    push 101
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
    push 108
addr_14:
    pop rbx
    pop rax
    mov [rax], bl
addr_15:
    push mem
addr_16:
    push 3
addr_17:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_18:
    push 108
addr_19:
    pop rbx
    pop rax
    mov [rax], bl
addr_20:
    push mem
addr_21:
    push 4
addr_22:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_23:
    push 111
addr_24:
    pop rbx
    pop rax
    mov [rax], bl
addr_25:
    push mem
addr_26:
    push 5
addr_27:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_28:
    push 44
addr_29:
    pop rbx
    pop rax
    mov [rax], bl
addr_30:
    push mem
addr_31:
    push 6
addr_32:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_33:
    push 32
addr_34:
    pop rbx
    pop rax
    mov [rax], bl
addr_35:
    push mem
addr_36:
    push 7
addr_37:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_38:
    push 87
addr_39:
    pop rbx
    pop rax
    mov [rax], bl
addr_40:
    push mem
addr_41:
    push 8
addr_42:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_43:
    push 111
addr_44:
    pop rbx
    pop rax
    mov [rax], bl
addr_45:
    push mem
addr_46:
    push 9
addr_47:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_48:
    push 114
addr_49:
    pop rbx
    pop rax
    mov [rax], bl
addr_50:
    push mem
addr_51:
    push 10
addr_52:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_53:
    push 108
addr_54:
    pop rbx
    pop rax
    mov [rax], bl
addr_55:
    push mem
addr_56:
    push 11
addr_57:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_58:
    push 100
addr_59:
    pop rbx
    pop rax
    mov [rax], bl
addr_60:
    push mem
addr_61:
    push 12
addr_62:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_63:
    push 10
addr_64:
    pop rbx
    pop rax
    mov [rax], bl
addr_65:
    push 12
addr_66:
    mov rax, 1
    mov rdi, 1
    mov rsi, mem
    pop rdx
    syscall
addr_67:
    mov rax, 60
    mov rdi, 0
    syscall
segment .bss
mem: resb 69000
