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
    push 49
addr_2:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_3:
    push 1
addr_4:
    pop rbx
    pop rax
    mov [rax], bl
addr_5:
    push 0
addr_6:
addr_7:
    pop rax
    push rax
    push rax
addr_8:
    push 49
addr_9:
    mov rcx, 0
    mov rdx, 1
    pop rax
    pop rbx
    cmp rbx, rax
    cmovl rcx, rdx
    push rcx
addr_10:
    pop rax
    test rax, rax
    jz addr_106
addr_11:
    push 0
addr_12:
addr_13:
    pop rax
    push rax
    push rax
addr_14:
    push 100
addr_15:
    mov rcx, 0
    mov rdx, 1
    pop rax
    pop rbx
    cmp rbx, rax
    cmovl rcx, rdx
    push rcx
addr_16:
    pop rax
    test rax, rax
    jz addr_44
addr_17:
    pop rax
    push rax
    push rax
addr_18:
    push mem
addr_19:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_20:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_21:
    pop rax
    test rax, rax
    jz addr_28
addr_22:
    push mem
addr_23:
    push 100
addr_24:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_25:
    push 42
addr_26:
    pop rbx
    pop rax
    mov [rax], bl
addr_27:
    jmp addr_33
addr_28:
    push mem
addr_29:
    push 100
addr_30:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_31:
    push 32
addr_32:
    pop rbx
    pop rax
    mov [rax], bl
addr_33:
    jmp addr_34
addr_34:
    push 1
addr_35:
    push mem
addr_36:
    push 100
addr_37:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_38:
    push 1
addr_39:
    push 1
addr_40:
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
addr_41:
    push 1
addr_42:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_43:
    jmp addr_12
addr_44:
    pop rax
addr_45:
    push mem
addr_46:
    push 100
addr_47:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_48:
    push 10
addr_49:
    pop rbx
    pop rax
    mov [rax], bl
addr_50:
    push 1
addr_51:
    push mem
addr_52:
    push 100
addr_53:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_54:
    push 1
addr_55:
    push 1
addr_56:
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
addr_57:
    push mem
addr_58:
    push 0
addr_59:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_60:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_61:
    push 1
addr_62:
    pop rcx
    pop rax
    shl rax, cl
    push rax
addr_63:
    push mem
addr_64:
    push 1
addr_65:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_66:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_67:
    pop rax
    pop rbx
    or rax, rbx
    push rax
addr_68:
    push 1
addr_69:
addr_70:
    pop rax
    push rax
    push rax
addr_71:
    push 98
addr_72:
    mov rcx, 0
    mov rdx, 1
    pop rax
    pop rbx
    cmp rbx, rax
    cmovl rcx, rdx
    push rcx
addr_73:
    pop rax
    test rax, rax
    jz addr_101
addr_74:
    pop rax
    pop rbx
    push rax
    push rbx
addr_75:
    push 1
addr_76:
    pop rcx
    pop rax
    shl rax, cl
    push rax
addr_77:
    push 7
addr_78:
    pop rax
    pop rbx
    and rax, rbx
    push rax
addr_79:
    pop rax
    pop rbx
    push rbx
    push rax
    push rbx
addr_80:
    push 1
addr_81:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_82:
    push mem
addr_83:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_84:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_85:
    pop rax
    pop rbx
    or rax, rbx
    push rax
addr_86:
    pop rax
    pop rbx
    push rbx
    push rax
    push rbx
    push rax
addr_87:
    push 90
addr_88:
    pop rax
    pop rbx
    push rax
    push rbx
addr_89:
    pop rcx
    pop rax
    shr rax, cl
    push rax
addr_90:
    push 1
addr_91:
    pop rax
    pop rbx
    and rax, rbx
    push rax
addr_92:
    pop rax
    pop rbx
    push rax
    push rbx
addr_93:
    push mem
addr_94:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_95:
    pop rax
    pop rbx
    push rax
    push rbx
addr_96:
    pop rbx
    pop rax
    mov [rax], bl
addr_97:
    pop rax
    pop rbx
    push rax
    push rbx
addr_98:
    push 1
addr_99:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_100:
    jmp addr_69
addr_101:
    pop rax
addr_102:
    pop rax
addr_103:
    push 1
addr_104:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_105:
    jmp addr_6
addr_106:
    pop rax
addr_107:
    mov rax, 60
    mov rdi, 0
    syscall
segment .bss
    mem: resb 138000
segment .data
