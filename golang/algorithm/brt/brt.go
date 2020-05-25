/**
 * Black Red Tree
 * version of 2-3 tree
 */
package brt

type Color int

const (
    Red Color = iota
    Black
)

type SymbleTable interface {
    Put(key int)
    Get(key int)
    Del(key int)
    Rank(key int)
    Range(lo, hi int) []int
}

type RedBlackTree struct {
    root *node
}

func (tree *RedBlackTree) Put(key int) {
    tree.root = put(tree.root, key)
    tree.root.color = Black
}

func New() *RedBlackTree {
    return &RedBlackTree{}
}

type node struct {
    key int
    left *node
    right *node
    N int
    color Color
}

func size(n *node) int {
    if n == nil {
        return 0
    } else {
        return n.N
    }
}

func put(n *node, key int) *node {
    if n == nil {
        return &node{key, nil, nil, 1, Red}
    }
    if key == n.key {
        return n
    }

    if key < n.key {
        n.left = put(n.left, key)
    } else if key > n.key {
        n.right = put(n.right, key)
    }
    n.N = size(n.left) + 1 + size(n.right)
    n = fix(n)

    return n
}

/**
 * rotate left
 *             x                  n
 *            / \     ----->     / \
 *           y   n              x   nr
 *              / \            / \
 *             nl nr          y  nl
 */
func rotateLeft(x *node) *node {
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
func rotateRight(x *node) *node {
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
    x.color = Red
    x.left.color = Black
    x.right.color = Black
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
    if !isRed(x.left) && isRed(x.right) {
        x = rotateLeft(x)
    }
    if x.left != nil && isRed(x.left) && isRed(x.left.left) {
        x = rotateRight(x)
    }
    if isRed(x.left) && isRed(x.right) {
        flip(x)
    }
    return x
}

func isRed(n *node) bool {
    if n == nil {
        return false
    } else {
        return n.color == Red
    }
}
