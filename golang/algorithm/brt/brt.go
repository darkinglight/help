/**
 * Black Red Tree
 * version of 2-3 tree
 */
package main

type color int

const {
    red color = iota
    black
}

type node struct {
    value int
    left *node
    right *node
    N int
    color color
}

/**
 * rotate left
 *             x                  n
 *            / \     ----->     / \
 *           y   n              x   nr
 *              / \            / \
 *             nl nr          y  nl
 */
func rotateLeft(x *node) {
    //node change
    n := x.right
    x.right = n.left
    n.left = x

    //color change, little trick
    n.color ^= x.color
    x.color ^= n.color
    n.color ^= x.color

    //N change
    n.N = x.N
    x.N = size(x.left) + 1 + size(x.right)

    return n
}

/**
 * rotate right
 *            x                  n
 *           / \     ----->     / \
 *          n   y              nl  x
 *         / \                    / \
 *       nl  nr                  nr  y
 */
func rotateRight(x *node) {
    n := x.left
    x.left = n.right
    n.right = x

    n.color ^= x.color
    x.color ^= n.color
    n.color ^= x.color

    n.N = x.N
    x.N = size(x.left) + 1 + size(x.right)

    return n
}

/**
 * flip
 * (r) red node
 * (b) black node
 *           x(b)                x(r)
 *           /  \     ----->     / \
 *        y(r)  z(r)          y(b)  z(b)
 */
func flip(x *node) {
    x.color = red
    x.left.color = black
    x.right.color = black
}

/**
 * fix wrong node
 * (r) red node
 * (b) black node
 * n new node
 * there are 3 condition need fix:
 *-------------------------------------------------------------
 * (1)     x(b)                                  x(b)
 *         / \           left rotate y           / \
 *       y(r) xr        -------------->        n(r) xr
 *       / \                                   / 
 *    z(b) n(r)                              y(r)
 *                                           /
 *                                         z(b)
 *-------------------------------------------------------------
 * (2)     x(b)                                   y(b)
 *         / \           right rotate x           / \
 *       y(r) xr        --------------->        n(r) x(r)
 *       / \                                        / \
 *     n(r) yr                                     yr  xr
 *-------------------------------------------------------------
 * (3)     x(b)                                  x(r)
 *         / \              flip x               / \
 *      y(r)  n(r)      -------------->        y(b) n(b)
 *-------------------------------------------------------------
 */
func fix(x *node) *node {
    if x.left.right.color == red && x.left.left.color = black {
        x.left = leftRotate(x.left)
    }
    if x.left.left.color == red && x.left.color == red {
        x = rightRotate(x)
    }
    if x.left.color == red && x.right.color == red {
        flip(x)
    }
    return x
}
