package main

import "fmt"

func main() {
	input := []string{"XOX", "O O", "XOX"}
	result := validTicTacToe(input)
	fmt.Println(result)
}

func validTicTacToe(board []string) bool {
	X, O := 0, 0
	sumX, sumO := 0, 0
	for i, str := range board {
		chars := []rune(str)
		for j, key := range chars {
			keyString := string(key)
			if keyString == "X" {
				X |= 1 << uint(i*3+j)
				sumX++

			} else if keyString == "O" {
				O |= 1 << uint(i*3+j)
				sumO++

			}

		}

	}

	//check num
	if !(sumX == sumO || sumX == (sumO+1)) {
		return false

	}

	//check finish
	var finished []int
	for i := 0; i < 3; i++ {
		finished = append(finished, 1<<uint(i*3)+1<<uint(i*3+1)+1<<uint(i*3+2))
		finished = append(finished, 1<<uint(i)+1<<uint(i+3)+1<<uint(i+6))

	}
	finished = append(finished, 1<<uint(0)+1<<uint(4)+1<<uint(8))
	finished = append(finished, 1<<uint(2)+1<<uint(4)+1<<uint(6))
	var stopX, stopO []int
	for _, finishing := range finished {
		if finishing&X == finishing {
			stopX = append(stopX, finishing)

		} else if finishing&O == finishing {
			stopO = append(stopO, finishing)

		}

	}
	if sumX == sumO {
		if len(stopX) > 0 {
			return false

		} else if (len(stopO) == 2) && (stopO[0]|stopO[1] == stopO[0]+stopO[1]) {
			return false

		}
		return true

	} else {
		if len(stopO) > 0 {
			return false

		} else if (len(stopX) == 2) && (stopX[0]|stopX[1] == stopX[0]+stopX[1]) {
			return false

		}
		return true

	}

}
