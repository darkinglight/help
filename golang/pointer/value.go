package main

import "fmt"

func main() {
	mainValue := int64(10)
	fmt.Printf("mainValue的内存地址: %p\n", &mainValue)
	fmt.Printf("modify前，mainValue的值: %v\n\n", mainValue)
	modify(mainValue)
	fmt.Printf("modify后，mainValue的值: %v\n\n", mainValue)
}

func modify(funcValue int64) {
	fmt.Printf("funcValue的内存地址: %p\n", &funcValue)
	funcValue = 1
}
