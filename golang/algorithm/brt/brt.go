//Black Red Tree
package main

type brnode struct {
    value int
    left *brnode
    right *brnode
    N int
    color char
}

/**
 * rotate left
 * (r) red node
 * (b) black node
 * (a) any node
 *           x(a)                z(a)
 *           /  \     ----->     / \
 *        y(b)  z(r)           x(r) zr
 *              / \            / \
 *             zl zr        y(b)  zl
 */
func rotateLeft(x *brnode) {
    //node change
    z := x.right
    x.right = z.left
    z.left = x

    //color change
    z.color = x.color
    x.color = 'r'

    //N change
    z.N = x.N
    x.N = size(x.left) + 1 + size(x.right)

    return z
}

/**
 * rotate right
 *           x(r)                y(b)
 *           /  \     ----->     / \
 *        y(b)   xr           z(r)  x(r)
 *        / \                       / \
 *     z(r)  yr                    yr  xr
 */
func rotateRight(x *brnode) {

}

/**
 * flip
 *           x(b)                x(r)
 *           /  \     ----->     / \
 *        y(r)  z(r)          y(b)  x(b)
 */
func flip() {

}
