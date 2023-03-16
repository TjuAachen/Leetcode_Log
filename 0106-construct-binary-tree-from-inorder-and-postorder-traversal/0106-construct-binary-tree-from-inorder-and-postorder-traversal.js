/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    var inorderLength = inorder.length;
    var postorderLength = postorder.length;

    if (inorderLength == 1) {
        return new TreeNode(inorder[0]);
    }
    if (inorderLength == 0) {
        return null
    }
    var curRoot = postorder[postorderLength - 1];
    
    for (var i = 0; i < inorderLength; i++) {
        if (inorder[i] == curRoot) {
            break;
        }
    }
    var leftInorder = inorder.slice(0, i);
    var rightInorder = inorder.slice(i + 1, inorderLength);

    var leftPostorder = postorder.slice(0, i);
    var rightPostorder = postorder.slice(i, postorderLength - 1);
    
    var leftNode = buildTree(leftInorder, leftPostorder)
    var rightNode = buildTree(rightInorder, rightPostorder)
    
    var rootNode = new TreeNode(curRoot, leftNode, rightNode)
    
    return rootNode;
    //find left inorder
    
    
    
    //
};