/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

function isMirror(root1, root2) {
    if (root1 == null && root2 == null)
        return true;
    if (root1 == null || root2 == null)
        return false;
    return (root1.val == root2.val) && arguments.callee(root1.left, root2.right) && arguments.callee(root1.right, root2.left);
}

var isSymmetric = function(root) {
    return isMirror(root, root)
};