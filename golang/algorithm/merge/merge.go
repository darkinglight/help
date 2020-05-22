package main

import (
    "fmt"
)

func test() {
    datas := []int{3,7,1,8,2,4,8,3,10,6}
    sort(datas, 0, len(datas) - 1)
    fmt.Println(datas)
}

func sort(datas []int, lo int, hi int) {
    if (lo >= hi) {
        return;
    }
    mid := (hi + lo) / 2
    
    sort(datas, lo, mid)
    sort(datas, mid + 1, hi)
    merge(datas, lo, mid, hi)
}

func merge(datas []int, lo int, mid int, hi int) {
    backup := make([]int, hi + 1)
    for i := lo; i <= hi; i++ {
        backup[i] = datas[i]
    }

    l := lo
    r := mid + 1
    for i := lo; i <= hi; i++ {
        if (l > mid) {
            datas[i] = backup[r]
            r++
        } else if (r > hi) {
            datas[i] = backup[l]
            l++
        } else if (backup[l] <= backup[r]) {
            datas[i] = backup[l]
            l++
        } else {
            datas[i] = backup[r]
            r++
        }
    }
}
