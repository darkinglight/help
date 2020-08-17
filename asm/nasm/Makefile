inc: inc.o
	ld -o $@ $<

inc.o: inc.asm print.inc
	nasm -felf64 -o $@ $<

callc: callc.o print.o
	ld -dynamic-linker /lib64/ld-linux-x86-64.so.2 -lc $^ -o $@

callc.o: callc.asm
	nasm -felf64 -o $@ $<

print.o: print.c
	gcc -c -o $@ $<

callasm: callasm.o callasm.c
	gcc -o $@ $^

callasm.o: callasm.asm
	nasm -felf64 -o $@ $<

hello: hello.o
	ld -o $@ $<

hello.o: hello.asm
	nasm -felf64 -o $@ $<

.Phony=clean
clean:
	rm -fr *.o  hello callasm callc inc
