package main

import "fmt"

func main() {
	result := myPow(2, 10)
	fmt.Println(result)
}

func myPow(x float64, n int) float64 {
	if n < 0 {
		x = 1 / x
		n = -n

	}

	var result float64 = 0
	unit := x
	for n > 0 {
		if n&1 == 1 {
			result += unit

		}

		unit = unit * unit
		n >>= 1

	}

	return result

}
