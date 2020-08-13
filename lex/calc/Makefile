calc: lex.yy.c y.tab.c
	gcc -o $@ $^

lex.yy.c: calc.l
	win_flex $<

y.tab.h: calc.y
	win_bison -vdty $<

y.tab.c: calc.y
	win_bison -vdty $<

y.output: calc.y
	win_bison -vdty $<

.PHONY=clean
clean:
	rm -fr y.tab.h y.tab.c y.output lex.yy.c calc
