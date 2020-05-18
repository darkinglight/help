//Binary Search Tree
package main

import (
    "fmt"
)

func main() {

}

type node struct {
    value int
    N int
    left *node
    right *node
}

// get num of node in this tree
func size(n *node) {
    if n == nil {
        return 0
    } else {
        return n.N
    }
}

// insert node
func put(n *node, value int) *node {
    if n == nil {
        return &node{value, 1, nil, nil}
    }
    if value < n.value {
        n.left = put(n.left, value)
    } else if value > n.value {
        n.right = put(n.right, value)
    }
    n.N = size(n.left) + 1 + size(n.right)
    return n
}

func get(n *node, rank int) *node {
    if n == nil || n.N <= rank {
        return nil
    }
    currentRank := size(n.left)
    if currentRank == rank {
        return n
    } else if currentRank > rank {
        return get(n.left, rank)
    } else {
        return get(n.right, rank - currentRank - 1)
    }
}

func min(n *node) *node {
    if n == nil {
        return nil
    }
    if n.left != nil {
        return min(n.left)
    } else {
        return n
    }
}

func delete(n *node, value int) *node {
    if n == nil {
        return nil
    }
    if value < n.value {
        n.left = delete(n.left, value)
        return n
    } else if value > n.value {
        n.right = delete(n.right, value)
        return n
    }
    //replace match node with right child's min node
    if n.right == nil {
        return n.left
    } else if n.left == nil {
        return n.right
    } else {
        
    }
}

type search interface {
    put(value int) error
    get(rank int) int
    delete(value int) (*node, error)
    rank(value int) int
    batch(lo int, hi int) []int
}

type bst struct {
    root *node
}

func (b *bst) put(value int) {
    b.root = put(b.root, value)
}

func (b *bst) get(rank int) int {
    n := get(b.root, rank)
    return n == nil ? nil : n.value
}
