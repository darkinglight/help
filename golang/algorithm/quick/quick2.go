package main

import "fmt"

func main() {
	nums := []int{2, 3, 3, 4, 6, 7}
	result := numSubseq(nums, 12)
	fmt.Println(result)
}

func numSubseq(nums []int, target int) int {
	length := len(nums)
	pqsort(nums, 0, length-1)

	result := 0
	i, j := 0, 0
	for i < length && nums[i]+nums[j] <= target {
		for j+1 < length && nums[i]+nums[j+1] <= target {
			j++
		}
		result = (result + cal(i, j)) % 1000000007
		i++
	}
	return result
}

func cal(i int, j int) int {
	result := 1
	for dist := j - i; dist > 0; dist-- {
		result <<= 1
	}
	return result
}

func pqsort(nums []int, low int, high int) {
	if high-low < 1 {
		return
	}
	mid := partition(nums, low, high)
	pqsort(nums, low, mid-1)
	pqsort(nums, mid+1, high)
}

func partition(nums []int, low int, high int) int {
	p, q := low+1, high
	pivot := nums[low]
	for {
		for p < high && nums[p] <= pivot {
			p++
		}
		for q > low && nums[q] >= pivot {
			q--
		}
		if p < q {
			swap(nums, p, q)
			p++
			q--
		} else {
			break
		}
	}
	swap(nums, low, q)
	return q
}

func swap(nums []int, p int, q int) {
	tmp := nums[p]
	nums[p] = nums[q]
	nums[q] = tmp
}
