package main

import (
    "fmt"
)

func test() {
    datas := []int{1, 5, 3, 2, 10, 7, 2, 4, 1, 9, 9, 7}
    sort(datas)
    fmt.Println(datas)
}

func sort(datas []int) {
	length := len(datas)
	for i := 0; i < length; i++ {
		for j := i; j > 0; j-- {
			if datas[j] < datas[j-1] {
				exchange(datas, j, j-1)
            } else {
                break
            }
		}
	}
}

func exchange(datas []int, i int, j int) {
	tmp := datas[i]
	datas[i] = datas[j]
	datas[j] = tmp
}
