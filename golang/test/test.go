package main

import "fmt"

func main() {
	v := [][]int{[]int{1, 3}, []int{3, 4}, []int{1, 5}, []int{3, 5}, []int{2, 3}}
	fmt.Println(f(v))
}

func f(edges [][]int) []int {
	hash := make(map[string]int)
	for index, edge := range edges {
		hash[str(edge)] = index
	}

	N := len(edges)
	adjacents := make([][]int, N+1)
	for _, edge := range edges {
		adjacents[edge[0]] = append(adjacents[edge[0]], edge[1])
		adjacents[edge[1]] = append(adjacents[edge[1]], edge[0])
	}

	colors := make([]bool, N+1)
	dfs(adjacents, colors, 1, 0)

	result := circle[0]
	for _, edge := range circle {
		if hash[str(edge)] > hash[str(result)] {
			result = edge
		}
	}
	return result
}

var start int
var circle [][]int

func dfs(adjacents [][]int, colors []bool, index int, p int) bool {
	if colors[index] == true {
		start = index
		return false
	}
	colors[index] = true

	for _, adjacent := range adjacents[index] {
		if adjacent == p {
			continue
		}
		if !dfs(adjacents, colors, adjacent, index) {
			if start > 0 {
				newedge := []int{adjacent, index}
				if index < adjacent {
					newedge = []int{index, adjacent}
				}
				circle = append(circle, newedge)
			}
			if index == start {
				start = 0
			}
			return false
		}
	}

	return true
}

func str(edge []int) string {
	return fmt.Sprintf("%d_%d", edge[0], edge[1])
}
