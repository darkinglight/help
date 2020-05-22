package bst

import (
    "fmt"
    "testing"
)

func TestPut(t *testing.T) {
    bst := prepare()
    value, _ := bst.Get(0)
    if value != 2 {
        t.Errorf("get value from position 0 error: %d", value)
    }
    value, _ = bst.Get(2)
    if value != 8 {
        t.Errorf("get value from position 2 error: %d", value)
    }
}

func TestDel(t *testing.T) {
    bst := prepare()
    fmt.Println(bst.Range(0, 3))
    // Output: [2 7 8 9]
    bst.Del(8)
    fmt.Println(bst.Range(0, 3))
    // Output: [2 7 9]

    value, _ := bst.Get(2)
    if value != 9 {
        t.Errorf("get value from position 2 error: %d", value)
    }
    bst.Put(1)
    bst.Del(2)
    value, _ = bst.Get(0)
    if value != 1 {
        t.Errorf("get value from position 2 error: %d", value)
    }
}

func TestRank(t *testing.T) {
    bst := prepare()
    value := bst.Rank(7)
    if value != 1 {
        t.Errorf("rank of 7 error: %d", value)
    }
}

func prepare() *BinarySearchTree {
    bst := NewBST()
    bst.Put(2)
    bst.Put(9)
    bst.Put(7)
    bst.Put(8)
    return bst
}
