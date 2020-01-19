package main

import (
	"flag"
	"fmt"
)

func main() {
	var intflag int
	flag.IntVar(&intflag, "intflag", 1234, "help message for intflag")
	flag.Parse()
	fmt.Println("intflag's value is ", intflag)
}
