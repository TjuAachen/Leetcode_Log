/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int preLen = preorder.length, inLen = inorder.length;
        if(preLen == 0){
            return null;
        }
        if(preLen == 1 && inLen == 1){
            return new TreeNode(preorder[0]);
        }
        TreeNode root = new TreeNode(preorder[0]);
        
        //find the root in inorder
        int i = 0;
        for(i = 0; i < inLen; i++){
            if(root.val == inorder[i]){
                break;
            }
        }
        TreeNode leftSubTree = buildTree(Arrays.copyOfRange(preorder,1, i+1), Arrays.copyOfRange(inorder, 0, i) );
        TreeNode rightSubTree = buildTree(Arrays.copyOfRange(preorder,i+1, preLen), Arrays.copyOfRange(inorder, i+1, inLen) );
        root.left = leftSubTree;
        root.right = rightSubTree;
        return root;
    }
}