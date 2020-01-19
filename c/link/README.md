# pre program
gcc -E -o main.i main.c

# ccl
gcc -S main.i main.s

# as
gcc -c main.s -o main.o

# ld
gcc tmp/main.o tmp/sum.o -o prog

# static lib
ar rcs libvector.a addvector.o multivector.o
