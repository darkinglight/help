package main

import "fmt"

func main() {
	array := []int{0}
	array = array[1:]
	if array == nil {
		fmt.Println("is nil")
	} else {
		result := array[0]
		fmt.Println(result)
	}
}
