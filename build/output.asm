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
    jz addr_105
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
    jz addr_41
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
    jz addr_30
addr_22:
    pop rax
    push rax
    push rax
addr_23:
    push mem
addr_24:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_25:
    push 100
addr_26:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_27:
    push 42
addr_28:
    pop rbx
    pop rax
    mov [rax], bl
addr_29:
    jmp addr_37
addr_30:
    pop rax
    push rax
    push rax
addr_31:
    push mem
addr_32:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_33:
    push 100
addr_34:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_35:
    push 32
addr_36:
    pop rbx
    pop rax
    mov [rax], bl
addr_37:
    jmp addr_38
addr_38:
    push 1
addr_39:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_40:
    jmp addr_12
addr_41:
    push mem
addr_42:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_43:
    push 100
addr_44:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_45:
    push 10
addr_46:
    pop rbx
    pop rax
    mov [rax], bl
addr_47:
    push 100
addr_48:
    push 1
addr_49:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_50:
    push mem
addr_51:
    push 100
addr_52:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_53:
    push 1
addr_54:
    push 1
addr_55:
    pop rax
    pop rdi
    pop rsi
    pop rdx
    syscall
addr_56:
    push mem
addr_57:
    push 0
addr_58:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_59:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_60:
    push 1
addr_61:
    pop rcx
    pop rax
    shl rax, cl
    push rax
addr_62:
    push mem
addr_63:
    push 1
addr_64:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_65:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_66:
    pop rax
    pop rbx
    or rax, rbx
    push rax
addr_67:
    push 1
addr_68:
addr_69:
    pop rax
    push rax
    push rax
addr_70:
    push 100
addr_71:
    mov rcx, 0
    mov rdx, 1
    pop rax
    pop rbx
    cmp rbx, rax
    cmovl rcx, rdx
    push rcx
addr_72:
    pop rax
    test rax, rax
    jz addr_100
addr_73:
    pop rax
    pop rbx
    push rax
    push rbx
addr_74:
    push 1
addr_75:
    pop rcx
    pop rax
    shl rax, cl
    push rax
addr_76:
    push 7
addr_77:
    pop rax
    pop rbx
    and rax, rbx
    push rax
addr_78:
    pop rax
    pop rbx
    push rbx
    push rax
    push rbx
addr_79:
    push 1
addr_80:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_81:
    push mem
addr_82:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_83:
    pop rax
    xor rbx, rbx
    mov bl, [rax]
    push rbx
addr_84:
    pop rax
    pop rbx
    or rax, rbx
    push rax
addr_85:
    pop rax
    pop rbx
    push rbx
    push rax
    push rbx
    push rax
addr_86:
    push 90
addr_87:
    pop rax
    pop rbx
    push rax
    push rbx
addr_88:
    pop rcx
    pop rax
    shr rax, cl
    push rax
addr_89:
    push 1
addr_90:
    pop rax
    pop rbx
    and rax, rbx
    push rax
addr_91:
    pop rax
    pop rbx
    push rax
    push rbx
addr_92:
    push mem
addr_93:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_94:
    pop rax
    pop rbx
    push rax
    push rbx
addr_95:
    pop rbx
    pop rax
    mov [rax], bl
addr_96:
    pop rax
    pop rbx
    push rax
    push rbx
addr_97:
    push 1
addr_98:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_99:
    jmp addr_68
addr_100:
    pop rax
addr_101:
    pop rax
addr_102:
    push 1
addr_103:
    pop rax
    pop rbx
    add rax, rbx
    push rax
addr_104:
    jmp addr_6
addr_105:
    pop rax
addr_106:
    mov rax, 60
    mov rdi, 0
    syscall
segment .bss
    mem: resb 138000
segment .data
