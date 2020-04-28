CC=gcc
LEX=win_flex
YACC=win_bison

.PHONY=all
all: calc3.tab.c calc3.tab.h lex.yy.c
	${CC} lex.yy.c calc3.tab.c intepreter.c -o cal

lex.yy.c: calc3.l
	${LEX} calc3.l

calc3.tab.c: calc3.y
	${YACC} -d calc3.y

calc3.tab.h: calc3.y
	${YACC} -d calc3.y

.PHONY=clean
clean: lex.yy.c
	rm cal.exe lex.yy.c calc3.tab.c calc3.tab.h

