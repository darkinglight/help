hello: hello.o
	ld -o $@ $<

hello.o: hello.s
	as -o $@ $<
clean:
	rm -fr hello hello.o
