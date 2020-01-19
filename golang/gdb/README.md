1. without debug information  `go build -ldflags=-w`
2. disable optimizations  `go build -gcflags=all="-N -l"`
