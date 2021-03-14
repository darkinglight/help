package main

import "fmt"
import "math"
import "flag"

var (
	h  bool
	pe float64
	g  float64
)

func init() {
	flag.BoolVar(&h, "h", false, "help")
	flag.Float64Var(&pe, "pe", 20, "p earning")
	flag.Float64Var(&g, "g", 20, "growth")
}

func main() {
	flag.Parse()
	if h {
		flag.Usage()
		return
	}
	g /= 100
	v := math.Log(g*pe+1)/math.Log(g+1) - 1
	fmt.Println(v)
}
