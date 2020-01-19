CC=go build
CFLAGS=-gcflags=all="-N -l"

all: bgraph
bgraph: bgraph.go
	$(CC) -o bin/bgraph $(CFLAGS) bgraph.go
