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
    h := 2

    for N := length / h; N >= 1; N /= h {
        for i := N; i < length; i++ {
            for j := i; j - N >= 0 && datas[j - N] > datas[j]; j -= N {
                exchange(datas, j - N, j)
            }
        }
    }

}

func exchange(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
