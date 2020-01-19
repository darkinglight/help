CC=go build
CFLAGS=-gcflags=all="-N -l"

all: test part
test: test.go
	$(CC) -o bin/test $(CFLAGS) test.go
part: part.go
	$(CC) -o bin/part $(CFLAGS) part.go
amount: amount.go
	$(CC) -o bin/amount $(CFLAGS) amount.go
team: team.go
	$(CC) -o bin/team $(CFLAGS) team.go
well: well.go
	$(CC) -o bin/well $(CFLAGS) well.go
pow: pow.go
	$(CC) -o bin/pow $(CFLAGS) pow.go
sort: sort.go
	$(CC) -o bin/sort $(CFLAGS) sort.go
clean:
	rm -fr bin/*
