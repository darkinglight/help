package main

import "fmt"

func main() {
	gas := []int{1, 2, 3, 4, 5}
	cost := []int{3, 4, 5, 1, 2}
	result := canCompleteCircuit(gas, cost)
	fmt.Println(result)
}

func canCompleteCircuit(gas []int, cost []int) int {
	length := len(gas)
	result := make([]int, length)
	for i := 0; i < length; i++ {
		result[i] = gas[i] - cost[i]

	}
	var temp int
	for i := 0; i < length; i++ {
		if result[i] > 0 {
			temp = 0
			j := 0
			for ; j < length; j++ {
				temp += result[(i+j)%length]
				if temp < 0 {
					break

				}

			}
			if j == (length - 1) {
				return i

			}

		}

	}
	return -1

}
