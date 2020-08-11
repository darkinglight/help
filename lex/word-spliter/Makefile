.PHONY=scanner
scanner: lex.yy.c token.h
	gcc -o $@ $<

lex.yy.c: scanner.l
	win_flex $<

.PHONY=clean
clean:
	rm -fr lex.yy.c scanner
