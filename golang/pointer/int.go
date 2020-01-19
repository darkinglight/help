package main

import "fmt"

func main() {
	i := 10
	iptr := &i
	fmt.Printf("main:iptr的内存地址: %p\n", &iptr)
	fmt.Printf("main:iptr(变量i的地址): %p\n\n", iptr)
	modify(iptr)
	fmt.Println("modify后的i值:", i)
	modifyValue(iptr)
	fmt.Println("modifyValue后的i值:", i)
}

func modify(iptr *int) {
	fmt.Printf("modify:iptr的内存地址: %p\n", &iptr)
	fmt.Printf("modify:iptr: %p\n\n", iptr)
	*iptr = 1
}

func modifyValue(iptr *int) {
	j := 100
	iptr = &j
}
