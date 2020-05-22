package bst

import (
    "fmt"
    "testing"
)

func TestPut(t *testing.T) {
    bst := NewBST()
    bst.Put(2)
    bst.Put(9)
    bst.Put(7)
    bst.Put(8)
    value, _ := bst.Get(0)
    if value != 2 {
        t.Error(fmt.Sprintf("get value from position 0 error: %d", value))
    }
    value, _ = bst.Get(2)
    if value != 8 {
        t.Error(fmt.Sprintf("get value from position 2 error: %d", value))
    }
}
