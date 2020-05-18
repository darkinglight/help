//Binary Search Tree
package main

import (
    "errors"
    "fmt"
)

func main() {
    b := &bst{}
    b.put(2)
    b.put(1)
    b.put(3)
    result := b.batch(0, 2)
    fmt.Println(result)
}

type node struct {
    value int
    N int
    left *node
    right *node
}

// get num of node in this tree
func size(n *node) int {
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

func deleteMin(n *node) (*node, int) {
    var deleteValue int
    if n.left != nil {
        n.left, deleteValue = deleteMin(n.left)
        n.N = size(n.left) + 1 + size(n.right)
    } else {
        deleteValue = n.value
        n = n.right
    }
    return n, deleteValue
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
    if n.right == nil {
        return n.left
    } else if n.left == nil {
        return n.right
    }
    //replace match node with right child's min node
    node, min := deleteMin(n.right)
    n.right = node
    n.value = min
    n.N = size(n.left) + 1 + size(n.right)

    return n
}

func rank(n *node, value int) int {
    if n == nil {
        return -1
    }
    if n.value == value {
        return size(n.left)
    } else if value < n.value {
        return rank(n.left, value)
    } else {
        return rank(n.right, value) + size(n.left) + 1
    }
}

func batch(n *node, lo, hi int) []int {
    if n == nil || n.N <= lo || hi < 0 {
        return []int{}
    }
    index := size(n.left)
    result := []int{}
    leftResult := batch(n.left, lo, hi)
    result = append(result, leftResult...)
    if lo <= index && index <= hi {
        result = append(result, n.value)
    }
    rightResult := batch(n.right, lo - index - 1, hi - index - 1)
    result = append(result, rightResult...)
    return result
}

type search interface {
    put(value int)
    get(rank int) int
    delete(value int)
    rank(value int) int
    batch(lo int, hi int) []int
}

type bst struct {
    root *node
}

func (b *bst) put(value int) {
    b.root = put(b.root, value)
}

func (b *bst) get(rank int) (int, error) {
    n := get(b.root, rank)
    if n == nil {
        return -1, errors.New("value not exist")
    } else {
        return n.value, nil
    }
}

func (b *bst) delete(value int) {
    b.root = delete(b.root, value)
}

func (b *bst) rank(value int) int {
    return rank(b.root, value)
}

func (b *bst) batch(lo, hi int) []int {
    return batch(b.root, lo, hi)
}
