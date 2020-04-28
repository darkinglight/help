.PHONY=all
all: cal.tab.c cal.tab.h lex.yy.c
	gcc lex.yy.c cal.tab.c -o cal

lex.yy.c: cal.l
	win_flex cal.l

cal.tab.c: cal.y
	win_bison -d cal.y

cal.tab.h: cal.y
	win_bison -d cal.y

.PHONY=clean
clean: lex.yy.c
	rm cal.exe lex.yy.c cal.tab.c cal.tab.h
