//堆排序

package main

import (
    "fmt"
)

func main() {
    datas := []int{3,7,6,17,2,3,5,6}
    sort(datas)
    fmt.Println(datas)
}

func sort(datas []int) {
    length := len(datas)
    buildHeap(datas)

    for i := length; i > 1; i-- {
        swap(datas, i - 1, 0)
        verify(datas, 1, i - 1)
    }
}

func buildHeap(datas []int) {
    length := len(datas)
    mid := length / 2

    for i := mid; i > 0; i-- {
        verify(datas, i, length)
    }
}

/**
 * index [1,MAX)
 */
func verify(datas []int, index int, length int) {
    left := index * 2
    right := left + 1
    if right <= length {
        if datas[left - 1] < datas[right - 1] {
            if datas[index - 1] < datas[right - 1] {
                swap(datas, index - 1, right -1)
                verify(datas, right, length)
            }
        } else {
            if datas[index - 1] < datas[left - 1] {
                swap(datas, index - 1, left - 1)
                verify(datas, left, length)
            }
        }
    } else if left <= length && datas[left - 1] > datas[index - 1] {
        swap(datas, index - 1, left - 1)
    }
}

func swap(data []int, i int, j int) {
    tmp := data[i]
    data[i] = data[j]
    data[j] = tmp
}
