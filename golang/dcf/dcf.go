package main

import (
	"flag"
	"fmt"
	"math"
)

var (
	h             bool
	profit        float64
	growthTen     float64
	growthForever float64
	discount      float64
)

func init() {
	flag.BoolVar(&h, "h", false, "help")
	flag.Float64Var(&profit, "p", 100, "current profit")
	flag.Float64Var(&growthTen, "g1", 25, "growth rate in ten year")
	flag.Float64Var(&growthForever, "g2", 5, "growth rate forever")
	flag.Float64Var(&discount, "r", 8, "discount rate")
}

func main() {
	flag.Parse()
	if h {
		flag.Usage()
		return
	}

	futures, currents, ten := tenYearValue(profit, growthTen, discount)

	forever := foreverValue(currents[9], growthForever, discount)

	fmt.Printf("%-10s", "第几年")
	for i := 0; i < 10; i++ {
		fmt.Printf("%-10d", i+1)
	}
	fmt.Println()

	fmt.Printf("%-10s", "现金流")
	for _, future := range futures {
		fmt.Printf("%-10.2f", future)
	}
	fmt.Println()

	fmt.Printf("%-10s", "折现值")
	for _, current := range currents {
		fmt.Printf("%-10.2f", current)
	}
	fmt.Println()

	fmt.Printf("10年累计现值:%.2f\n", ten)
	fmt.Printf("永续阶段现值:%.2f\n", forever)
	fmt.Printf("现金流折现值:%.2f\n", ten+forever)
}

/**
 * 10 year value
 */
func tenYearValue(v float64, g float64, r float64) (futures [10]float64, currents [10]float64, total float64) {
	factorG := 1 + g/100
	factorR := 1 + r/100
	for i := 0; i < 10; i++ {
		futures[i] = math.Round(v*factorG*100) / 100
		currents[i] = math.Round(futures[i]/factorR*100) / 100
		total += currents[i]
		factorG *= 1 + g/100
		factorR *= 1 + r/100
	}
	total = math.Round(total*100) / 100
	return
}

/**
 * forever current value
 * v: current value after ten year
 * g: generation
 * r: reduce
 */
func foreverValue(v float64, g float64, r float64) float64 {
	return v * (1 + g/100) / (r/100 - g/100)
}
