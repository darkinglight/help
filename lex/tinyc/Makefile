CC = gcc
LEX = flex
YACC = bison
OUT = tcc
OBJ = lex.yy.o y.tab.o
SCANNER = scanner.l
PARSER = parser.y

.PHONY: build test clean

build: $(OUT)

test: $(OUT)
	./$(OUT) < test.c > test.asm

$(OUT): $(OBJ)
	$(CC) -o $@ $^

lex.yy.c: $(SCANNER) y.tab.c
	$(LEX) $<

y.tab.c: $(PARSER)
	$(YACC) -vdty $<

clean:
	rm -fr *.o lex.yy.c y.tab.c y.tab.h y.output $(OUT)
