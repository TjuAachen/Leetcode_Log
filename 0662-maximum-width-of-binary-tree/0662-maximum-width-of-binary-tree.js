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
var widthOfBinaryTree = function(root) {
    var queue = []
    var maxWidth = 1
    var MOD = 2147483647
    //bfs
    queue.push([root, 0])
    
    while (queue.length > 0) {
        var size = queue.length

        // go to the next level
        var leftNum = Infinity
        var rightNum = -Infinity
        for (var i = 0; i < size; i++) {
            var [poppedNode, num] = queue.shift()
            if (poppedNode.left) {
                var curNum = (num * 2 + 1) % MOD
                queue.push([poppedNode.left, curNum])
                leftNum = Math.min(num * 2 + 1, leftNum)
                rightNum = Math.max(num * 2 + 1, rightNum)
            }
            if (poppedNode.right) {
                var curNum = (num * 2 + 2) % MOD
                queue.push([poppedNode.right, curNum])
                leftNum = Math.min(curNum, leftNum)
                rightNum = Math.max(curNum, rightNum)
            }
        }
        if (leftNum != Infinity && rightNum != -Infinity && leftNum != rightNum) {
       
            maxWidth = Math.max(maxWidth, Math.abs(rightNum - leftNum) % MOD + 1)
           
        }
    }
    
    return maxWidth
    
    
};