//Black Red Tree
package main

type struct node {
    value int
    left *node
    right *node
    N int
    color char
}

/**
 *×óÐý
 *           x(b)                z(r)
 *           /  \     ----->     / \
 *          y  z(r)           x(b) zr
 *              / \            / \
 *             zl zr          y  zl
 */
func rotateLeft(x *node) {
    z := x.right
    x.right = z.left
    z.left = x

    return z
}

/**
 * ÓÒÐý
 *           x(r)                y(b)
 *           /  \     ----->     / \
 *        y(b)   xr           z(r)  x(r)
 *        / \                       / \
 *     z(r)  yr                    yr  xr
 */
func rotateRight(x *node) {

}

/**
 * ·­×ª
 *           x(b)                x(r)
 *           /  \     ----->     / \
 *        y(r)  z(r)          y(b)  x(b)
 */
func flip() {

}
