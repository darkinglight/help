package main

import "fmt"
import "unsafe"

func main() {
	valueInt8 := int8(10)
	valueInt := 100
	valueInt2 := 200
	var pointerInt *int

	fmt.Printf("int8: size=%d align=%d address=%p\n", unsafe.Sizeof(valueInt8), unsafe.Alignof(valueInt8), &valueInt8)

	fmt.Printf("int: size=%d align=%d address=%p\n", unsafe.Sizeof(valueInt), unsafe.Alignof(valueInt), &valueInt)

	fmt.Printf("int2: size=%d address=%p\n", unsafe.Sizeof(valueInt2), &valueInt2)

	fmt.Printf("pointerInt: size=%d address=%p\n", unsafe.Sizeof(pointerInt), &pointerInt)
}
