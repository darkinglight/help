package queue

import (
    "testing"
)

func TestInt(t *testing.T) {
    queue := NewIntQueue()
    queue.Push(1)
    queue.Push(2)
    value, _ := queue.Pop()
    if value != 1 {
        t.Errorf("expect value is 1, result is %d", value)
    }
}
