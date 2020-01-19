	.file	"example.c"
	.text
	.globl	add_a_and_b
	.type	add_a_and_b, @function
add_a_and_b:
.LFB0:
	.cfi_startproc
	leal	(%rdi,%rsi), %eax
	ret
	.cfi_endproc
.LFE0:
	.size	add_a_and_b, .-add_a_and_b
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	movl	$5, %eax
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
