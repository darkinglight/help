#rio
objects = cpfile.o rio.o
cpfile: $(objects)
	gcc -o cpfile $(objects)

# can deleted
cpfile.o: cpfile.c
	gcc -c -o cpfile.o cpfile.c

# can deleted
cpfile.o: cpfile.c
rio.o: rio.c
	gcc -c -o rio.o rio.c

.PHONY: clean
clean:
	-rm cpfile *.o
