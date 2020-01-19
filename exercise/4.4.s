rsum:
	testq	%rsi, %rsi
	jle	.L3
	pushq	%rbx
	movq	%rdi, %rbx
	subq	$1, %rsi
	leaq	8(%rdi), %rdi
	call	rsum
	addq	(%rbx), %rax
	jmp	.L2
.L3:
	movl	$0, %eax
	ret
.L2:
	popq	%rbx
	ret
