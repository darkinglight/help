package brt

import (
    "testing"
)

/**
 *                 4(b)
 *              /        \
 *         2(b)            8(b)
 *        /    \          /    \
 *     1(b)    3(b)    6(r)    9(b)
 *                    /    \
 *                 5(b)    7(b)
 */
func TestPut(t *testing.T) {
    tree := New()
    tree.Put(1)
    tree.Put(2)
    tree.Put(3)
    tree.Put(4)
    tree.Put(5)
    tree.Put(6)
    tree.Put(7)
    tree.Put(8)
    tree.Put(9)

    expectNode(t, tree.root, 4, Black, 9)
    expectNode(t, tree.root.left, 2, Black, 3)
    expectNode(t, tree.root.right, 8, Black, 5)
    expectNode(t, tree.root.right.left, 6, Red, 3)
}

func expectNode(t *testing.T, n *node, key int, color Color, N int) {
    if n.key != key {
        t.Errorf("node key expect %d, receive %d\n", key, n.key)
    }
    if n.color != color {
        t.Errorf("node color expect %d, receive %d\n", color, n.color)
    }
    if n.N != N {
        t.Errorf("node N expect %d, receive %d\n", N, n.N)
    }

}
