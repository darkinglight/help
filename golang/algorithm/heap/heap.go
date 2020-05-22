package heap

import (
    "fmt"
)

func test() {
    datas := []int{3,7,6,17,2,3,5,6}
    datas = sort(datas)
    fmt.Println(datas)
}

func sort(datas []int) []int {
    length := len(datas)

    //datas[0] never used
    datas = append([]int{0}, datas...)

    for i := length / 2; i > 0; i-- {
        sink(datas, i, length)
    }

    for i := length; i > 1; i-- {
        swap(datas, i, 1)
        sink(datas, 1, i - 1)
    }

    //delete datas[0] add before
    return datas[1:]
}

/**
 * index [1,MAX)
 */
func sink(datas []int, index int, length int) {
    sub := index * 2
    if sub > length {
        return
    } else if sub + 1 <= length && datas[sub] < datas[sub + 1] {
        sub++
    }

    if datas[index] < datas[sub] {
        swap(datas, sub, index)
        sink(datas, sub, length)
    }
}

func swap(data []int, i int, j int) {
    tmp := data[i]
    data[i] = data[j]
    data[j] = tmp
}
