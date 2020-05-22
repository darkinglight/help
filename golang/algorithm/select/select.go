package main

import (
    "fmt"
)

func test() {
    datas := []int{3,1,7,5,10,10,3,9}
    sort(datas)
    fmt.Println(datas)
}

func sort(datas []int) {
    length := len(datas)
    for i := 0; i < length - 1; i++ {
        min := i
        for j := i + 1; j < length; j++ {
            if datas[min] > datas[j] {
                min = j
            }
        }
        exchange(datas, i, min)
    }
}

func exchange(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
