CC=go build
CFLAGS=-gcflags=all="-N -l"

.PHONY: all
all: bgraph merge

bgraph: bgraph.go
	$(CC) -o bin/bgraph $(CFLAGS) bgraph.go

merge: merge.go
	$(CC) -o bin/merge $(CFLAGS) merge.go
	CGO_ENABLED=0 GOOS=windows GOARCH=amd64 $(CC) -o bin/merge.exe $(CFLAGS) merge.go
