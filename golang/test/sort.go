package main

import "fmt"

func main() {
	input := []int{-4, 0, 7, 4, 9, -5, -1, 0, -7, -1}
	result := sortArray(input)
	fmt.Println(result)
}

func sortArray(nums []int) []int {
	buildHeap(nums)
	heapSort(nums)
	return nums

}

func left(i int) int {
	return (i+1)*2 - 1

}

func right(i int) int {
	return (i + 1) * 2

}

func parent(i int) int {
	return (i+1)/2 - 1

}

func buildHeap(nums []int) {
	length := len(nums)

	var max int
	for i := parent(length - 1); i >= 0; i-- {
		leftIndex := left(i)
		rightIndex := right(i)
		max = i
		if leftIndex < length && nums[leftIndex] > nums[max] {
			max = leftIndex

		}
		if rightIndex < length && nums[rightIndex] > nums[max] {
			max = rightIndex

		}
		if max != i {
			nums[i], nums[max] = nums[max], nums[i]
			heapify(nums, max, length)

		}

	}

}

func heapSort(nums []int) {
	length := len(nums)
	for i := length - 1; i > 0; i-- {
		nums[0], nums[i] = nums[i], nums[0]
		heapify(nums, 0, i)

	}

}

func heapify(nums []int, i int, length int) {
	leftIndex := left(i)
	rightIndex := right(i)
	max := i
	if leftIndex < length && nums[leftIndex] > nums[max] {
		max = leftIndex

	}
	if rightIndex < length && nums[rightIndex] > nums[max] {
		max = rightIndex

	}
	if max != i {
		nums[i], nums[max] = nums[max], nums[i]
		heapify(nums, max, length)

	}

}

func insertSort(nums []int) []int {
	var result []int
	for _, item := range nums {
		i := len(result)
		for i > 0 && result[i-1] > item {
			i--
		}
		var newResult []int = make([]int, len(result)+1)
		copy(newResult, result[0:i])
		newResult[i] = item
		copy(newResult[i+1:], result[i:])
		result = newResult

	}
	return result

}

func sort(nums []int, i int, j int) {
	if len(nums) < 2 {
		return

	}
	pivot := nums[i]
	left := i
	right := j
	for left < right {
		for (left < right) && (nums[left] <= pivot) {
			left++

		}
		for (left < right) && (nums[right] > pivot) {
			right--

		}
		if left < right {
			nums[left], nums[right] = nums[right], nums[left]

		}

	}
	nums[i], nums[right] = nums[right], nums[i]
	sort(nums, i, right-1)
	sort(nums, right+1, j)

}
