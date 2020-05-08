//快速排序
package main

import (
    "fmt"
)

func main() {
    datas := []int{3, 1, 7, 6, 3, 2, 9, 8, 5, 3, 4, 2, 1, 3}
    sort(datas, 0, len(datas) - 1)
    fmt.Println(datas)
}

func sort(datas []int, lo int, hi int) {
    if (lo >= hi) {
        return
    }

    mid := partition(datas, lo, hi)
    sort(datas, lo, mid - 1)
    sort(datas, mid + 1, hi)
}

func partition(datas []int, lo int, hi int) int {
    v := datas[lo]
    i := lo + 1
    j := hi
    for true {
        for datas[i] < v {
            i++
            if (i > hi) {
                break 
            }
        }

        for datas[j] > v {
            j--
        }

        if (i < j) {
            swap(datas, i, j)
            i++
            j--
        } else {
            swap(datas, lo, j)
            break
        }
    }
    return j
}

func swap(datas []int, i int, j int) {
    tmp := datas[i]
    datas[i] = datas[j]
    datas[j] = tmp
}
