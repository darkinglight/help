package main

import "fmt"
import "sort"

func main() {
	test := []int{10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6}
	k := 3
	result := canPartitionKSubsets(test, k)
	fmt.Println(result)
}

func canPartitionKSubsets(nums []int, k int) bool {
	sum := 0
	max := 0
	for _, value := range nums {
		sum += value
		if max < value {
			max = value

		}

	}
	avg := sum / k
	length := len(nums)
	if (sum%k != 0) || (max > avg) || length < k {
		return false

	}

	sort.Ints(nums)
	used := make([]bool, length)
	for i := 0; i < length; i++ {
		used[i] = false

	}
	return dfs(nums, length-1, avg, used, k, avg)

}

func dfs(nums []int, index int, target int, used []bool, remainK int, originTarget int) bool {
	if index < 0 {
		return false

	}
	if used[index] == true || nums[index] > target {
		return dfs(nums, index-1, target, used, remainK, originTarget)

	}

	target -= nums[index]
	used[index] = true
	if target == 0 {
		remainK--
		target = originTarget

	}
	if remainK == 0 {
		return true

	}

	for i := index - 1; i >= 0; i-- {
		result := dfs(nums, i, target, used, remainK, originTarget)
		if result == true {
			return true

		}

	}

	return false

}
