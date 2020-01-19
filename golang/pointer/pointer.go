package main

import "fmt"

func main() {
	var p *int
	fmt.Println("pointer p's address is %p", &p)
	fmt.Println("pointer p's value is %p", p)
	change(p)
}

func change(p *int) {
	fmt.Println("pointer p's address in change function is %p", &p)
}
