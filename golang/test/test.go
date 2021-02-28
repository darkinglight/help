package main

import "fmt"
import "sort"

func main() {
	data := []int{1, 0, 0}
	fmt.Println(hIndex(data))
}

func hIndex(citations []int) int {
	sort.Ints(citations)
	l := len(citations)
	var h int = 0
	for i := 0; i < l; i++ {
		if l-i >= citations[i] {
			h = citations[i]
		} else {
			break
		}
	}
	return h
}
