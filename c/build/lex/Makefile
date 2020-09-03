CC=gcc -g

.PHONY:test
test: nfa.o
	$(CC) nfa.o -o test

nfa.o: nfa.c nfa.h
	$(CC) -c nfa.c -o nfa.o

.PHONY:clean
clean:
	rm *.o test
