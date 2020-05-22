package bubble

import (
    "fmt"
)

//func test() {
//    datas := []int{1, 5, 3, 2}
//    sort(datas)
//    fmt.Println(datas)
//}

func sort(datas []int) {
	length := len(datas)
	for i := 0; i < length-1; i++ {
		for j := length - 1; j > i; j-- {
			if datas[j] < datas[j-1] {
				exchange(datas, j, j-1)
			}
		}
	}
}

func exchange(datas []int, i int, j int) {
	tmp := datas[i]
	datas[i] = datas[j]
	datas[j] = tmp
}
