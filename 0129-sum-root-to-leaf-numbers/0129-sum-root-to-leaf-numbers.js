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
 * @return {number}
 */
var sumNumbers = function(root) {
    var queue = [];
    queue.push([root, root.val]);
    var res = 0;
    
    while (queue.length > 0) {
        var [popped, curVal] = queue.shift();

        if (popped.left != null) {
            queue.push([popped.left, curVal * 10 + popped.left.val])
        }
        if (popped.right != null) {
            queue.push([popped.right, curVal * 10 + popped.right.val])
        }
        if (popped.left == null && popped.right == null){
            res += curVal;
        }
    }
    
    return res;
    
};