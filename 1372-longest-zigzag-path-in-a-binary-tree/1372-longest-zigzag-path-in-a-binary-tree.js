"use strict";
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
// direction: 1 left, -1 right

function longestDist(root, direction) {

    if (root == null)
        return -1
 
   // console.log([ll, lr + 1, rl + 1, rr], root.val)
    //res = [ll, lr, rl, rr].reduce((a, b) => (Math.max(a, b), - 1))
    if (direction == 1) {
    var ll = longestDist(root.left, 1)
    var lr = longestDist(root.left, -1)
   // console.log(ll, lr + 1, root.val, direction)
    res = Math.max(res, ll)
    res = Math.max(res, lr)
    return lr + 1
    }
    var rl = longestDist(root.right, 1)
    var rr = longestDist(root.right, -1)
  //  console.log(rl + 1, rr, root.val, root.right, direction)
    res = Math.max(res, rl)
    res = Math.max(res, rr)
    return rl + 1
}

var longestZigZag = function(root) {
    res = 0
    var curRes = Math.max(longestDist(root, 1),longestDist(root, -1))
  //  console.log(longestDist(root.left, -1))
    return Math.max(res, curRes)
    
};