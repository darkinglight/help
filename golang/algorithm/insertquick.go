//三取样快排

package main

import (
    "fmt"
)

func main() {
    datas := []int{2,3,5,1,3,7,9,3,4,6,1,3,6,9,6,5,3,4,2,9,7,6,2,1,5,7,9,8,7,5,3,2,1}
    lo := 0
    hi := len(datas) - 1
    mid := (lo + hi) / 2
    if lo < mid {
        if mid < hi {
            swap(datas, lo, mid)
        } else if lo < hi {
            swap(datas, lo, hi)
            swap(datas, mid, hi)
        } else {
            swap(datas, mid, hi)
        }
    } else {
        if mid > hi {
            swap(datas, lo, mid)
            swap(datas, mid, hi)
        } else if hi < lo {
            swap(datas, lo, hi)
        } else {
            //nothing
        }
    }
    sort(datas, 0, len(datas) - 1)
    fmt.Println(datas)
}

func sort(datas []int, lo int, hi int) {
    if (hi - lo < 5) {
        insert(datas, lo, hi)
    } else {
        mid := partition(datas, lo, hi)
        sort(datas, lo, mid - 1)
        sort(datas, mid + 1, hi)
    }
}

func insert(datas []int, lo int, hi int) {
    for i := lo + 1; i <= hi; i++ {
        for j := i; j > lo && datas[j] < datas[j - 1]; j-- {
            swap(datas, j - 1, j)
        }
    }
}

func partition(datas []int, lo int, hi int) int {
    v := datas[lo]
    i := lo + 1
    j := hi

    for i < j {
        if datas[i] < v {
            i++
        }
        if datas[j] > v {
            j--
        }
        if i < j {
            swap(datas, i, j)
        }
    }
    swap(datas, lo, j)
    return j
}

func swap(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
