package main

import "fmt"
import "sort"
import "strconv"

func main() {
	fmt.Println(minCost(7, []int{1, 3, 4, 5}))
}

func minCost(n int, cuts []int) int {
	sort.Ints(cuts)
	list := make([]int, len(cuts)+2)
	list[0] = 0
	copy(list[1:], cuts)
	list[len(list)-1] = n
	dp := make(map[string]int)
	length := len(list)
	for l := 2; l < length; l++ {
		for i := 0; i < length-l; i++ {
			for j := 1; j < l; j++ {
				result := dp[key(list[i], list[j])] + dp[key(list[j], list[i+l])] + list[i+l] - list[i]
				if dp[key(list[i], list[i+l])] == 0 || dp[key(list[i], list[i+l])] > result {
					dp[key(list[i], list[i+l])] = result
				}
			}
		}
	}
	return dp[key(0, n)]
}

func key(left int, right int) string {
	return strconv.Itoa(left) + "_" + strconv.Itoa(right)
}
