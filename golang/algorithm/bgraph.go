package main

import "fmt"

func test() {
	graph := [][]int{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}}
	result := isBipartite(graph)
	fmt.Println(result)
}

func isBipartite(graph [][]int) bool {
	colors := make(map[int]int)
	for i := 0; i < len(graph); i++ {
		_, ok := colors[i]
		if ok == false {
			if bfs(graph, colors, i) == false {
				return false

			}

		}

	}
	return true

}

func bfs(graph [][]int, colors map[int]int, index int) bool {
	_, ok := colors[index]
	if ok == false {
		colors[index] = 0

	}

	queue := []int{index}
	for len(queue) > 0 {
		i := queue[0]
		queue = queue[1:]
		colorDestiny := (colors[i] + 1) % 2
		for _, j := range graph[i] {
			subColor, ok := colors[j]
			if ok == true {
				if subColor != colorDestiny {
					return false

				}

			} else {
				colors[j] = colorDestiny
				queue = append(queue, j)

			}

		}

	}
	return true

}
