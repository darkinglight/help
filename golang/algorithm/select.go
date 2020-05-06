package main

import (
    "fmt"
)

func main() {
    datas := []int{3,1,7,5,10,10,3,9}
    sort(datas)
    fmt.Println(datas)
}

func sort(datas []int) {
    length := len(datas)
    for i := 0; i < length - 1; i++ {
        for j := i + 1; j < length; j++ {
            if datas[i] > datas[j] {
                exchange(datas, i, j)
            }
        }
    }
}

func exchange(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
