//Binary Search Tree
package bst

import (
    "errors"
)

type SymbleTable interface {
    Put(value int)
    Get(rank int) int
    Del(value int)
    Rank(value int) int
    Range(lo int, hi int) []int
}

type BinarySearchTree struct {
    root *node
}

func NewBST() *BinarySearchTree {
    return &BinarySearchTree{}
}

func (bst *BinarySearchTree) Put(value int) {
    bst.root = put(bst.root, value)
}

func (bst *BinarySearchTree) Get(rank int) (int, error) {
    n := get(bst.root, rank)
    if n == nil {
        return -1, errors.New("value not exist")
    } else {
        return n.value, nil
    }
}

func (bst *BinarySearchTree) Del(value int) {
    bst.root = delete(bst.root, value)
}

func (bst *BinarySearchTree) Rank(value int) int {
    return rank(bst.root, value)
}

func (bst *BinarySearchTree) Range(lo, hi int) []int {
    return batch(bst.root, lo, hi)
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
    } else if value > n.value {
        n.right = delete(n.right, value)
    } else if n.right == nil {
        return n.left
    } else if n.left == nil {
        return n.right
    } else {
        //replace match node with right child's min node
        node, min := deleteMin(n.right)
        n.right = node
        n.value = min
    }
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
