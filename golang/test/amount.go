package main

import "fmt"

func main() {
	result := getMoneyAmount(2)
	fmt.Println(result)
}

func getMoneyAmount(n int) int {
	result := make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		result[i] = make([]int, n+1)
	}

	for length := 1; length < n+1; length++ {
		for start := 1; start < n-length+1; start++ {
			result[start][start+length-1] = int(^uint(0) >> 1)
			for pivot := start; pivot < start+length; pivot++ {
				left := result[start][pivot-1]
				right := result[pivot+1][start+length-1]
				var item int
				if left > right {
					item = left + pivot

				} else {
					item = right + pivot

				}
				if item < result[start][start+length-1] {
					result[start][start+length-1] = item

				}

			}

		}

	}
	return result[1][n]

}
