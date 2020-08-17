%include "print.inc"

section .data

section .text
	global _start
_start:
	print message, 13
	jmp exit

message: db "Hello, World", 0xa

exit:
	mov rax, 60
	mov rdi, 0
	syscall
