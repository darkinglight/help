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

    h := 3
    N := 1
    for N * h < length {
        N = N * h
    }

    for ; N >= 1; N /= h {
        for i := length - 1; i > 0; i-- {
            for j := i - N; j >= 0; j -= N {
                if datas[j] > datas[i] {
                    exchange(datas, i, j)
                }
            }
        }
    }

}

func exchange(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
