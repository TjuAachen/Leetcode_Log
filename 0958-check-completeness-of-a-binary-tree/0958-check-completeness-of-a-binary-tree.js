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
var isCompleteTree = function(root) {
    if (root == null)
        return false
    
    var nullFound = false
    var queue = []
    queue.push(root)
    
    while (queue.length > 0) {
        var curNode = queue.shift()
        
        if (curNode == null) {
            nullFound = true
        }else {
            if (nullFound)
                return false
            queue.push(curNode.left);
            queue.push(curNode.right);
        }
    }
    
    return true;
};