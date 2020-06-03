package graph

import (
    "fmt"
)

type Graph interface {
    Edges()
}

type graph struct {
    N int
    vertices [][]edge
}

func New(vertexNum int) *graph {
    vertices := [vertexNum][]edge
    return &graph{vertexNum, vertices}
}

type edge struct {
    vertices [2]int
    weight int
}
func New(v1 int, v2 int, weight int) *edge {
    return &edge{[2]int{v1, v2}, weight}
}
