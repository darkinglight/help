//三向快排

package main

import (
    "fmt"
)

func test() {
    datas := []int{3,5,8,2,3,6,5,2,4,6,2,7,2,34,45,2,56,43}
    sort(datas, 0, len(datas) - 1)
    fmt.Println(datas)
}

func sort(datas []int, lo int, hi int) {
    if (lo >= hi) {
        return
    }

    lt, gt := partition(datas, lo, hi)
    sort(datas, lo, lt - 1)
    sort(datas, gt + 1, hi)
}

func partition(datas []int, lo int, hi int) (int, int) {
    lt := lo + 1
    gt := hi
    i := lo + 1
    v := datas[lo]

    for i <= gt {
        if datas[i] == v {
            i++
        } else if (datas[i] < v) {
            swap(datas, i, lt)
            i++
            lt++
        } else {
            swap(datas, i, gt)
            gt--
        }
    }
    lt--
    swap(datas, lo, lt)
    return lt, gt
}

func swap(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
