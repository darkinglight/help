package queue

import (
    "errors"
)

type Queue interface {
    Push(value int)
    Pop() (int, error)
    Get(index int) (int, error)
}
type queue struct {
    head *node
    tail *node
}

func NewIntQueue() *queue {
    return &queue{nil, nil}
}
func (q *queue) Push(value int) {
    newNode := &node{value, nil}
    if q.tail == nil {
        q.head = newNode
        q.tail = newNode
    } else {
        q.tail.next = newNode
        q.tail = newNode
    }
}

func (q *queue) Pop() (int, error) {
    if q.head == nil {
        outOfRangeErr := errors.New("out of queue range")
        return 0, outOfRangeErr
    }

    n := q.head
    q.head = q.head.next
    if q.head == nil {
        q.tail = nil
    }
    return n.value, nil
}

type node struct {
    value int
    next *node
}
