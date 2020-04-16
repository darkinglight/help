CC=gcc

.PHONY:test
test: main.o intepret.o util.o
	$(CC) $^ -o $@

main.o: main.c
	$(CC) -c $^ -o $@

intepret.o: intepret.c
	$(CC) -c $^ -o $@

util.o: util.c
	$(CC) -c $^ -o $@

.PHONY:clean
clean:
	rm -f *.o *.exe
