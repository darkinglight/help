.PHONY=all
all: lex.yy.c
	gcc -o hide-digits lex.yy.c

lex.yy.c: hide-digits.l
	win_flex hide-digits.l

.PHONY=clean
clean:
	rm -fr lex.yy.c hide-digits
