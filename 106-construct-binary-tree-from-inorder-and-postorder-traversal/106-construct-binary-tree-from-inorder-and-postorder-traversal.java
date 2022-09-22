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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int inLen = inorder.length;
        if(inLen == 0)return null;
        TreeNode root = new TreeNode(postorder[inLen - 1]);
        int i = 0;
        for(i = 0; i < inLen; i++){
            if(inorder[i] == root.val)break;   
        }
        TreeNode leftSubTree = buildTree(Arrays.copyOfRange(inorder, 0, i), Arrays.copyOfRange(postorder, 0, i));
        TreeNode rightSubTree = buildTree(Arrays.copyOfRange(inorder, i + 1, inLen), Arrays.copyOfRange(postorder, i, inLen - 1));
        root.left = leftSubTree;
        root.right= rightSubTree;
        return root;
    }
}