CC=gcc
IDIR=../include
CFLAGS=-I$(IDIR)

_DEPS = epoll_lib.h
DEPS = $(patsubst %, $(IDIR)/%, $(_DEPS))

LDIR=../lib
LDFLAGS=-L$(LDIR)

ODIR=obj
_OBJ = epoll_demo.o epoll_lib.o
OBJ = $(patsubst %, $(ODIR)/%, $(_OBJ))

LIBS=-lm

$(ODIR)/%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

epoll_demo: $(OBJ)
	$(CC) -g -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f epoll_demo $(ODIR)/*.o
