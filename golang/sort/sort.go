package main

import (
	"fmt"
	"sort"
)

type Score []int

func (s Score) Len() int {
	return len(s)
}

func (s Score) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s Score) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func main() {
	ints := Score{10, 2, 5, 12, 130, 63, 12, 7, 12, 98, 120, 35, 26, 15, 12, 240, 23}
	sort.Sort(ints)
	fmt.Println(ints)
}
