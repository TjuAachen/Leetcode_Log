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
    public int goodNodes(TreeNode root) {
        return this.numGoodNodes(root, Integer.MIN_VALUE);
        
    }
    public int numGoodNodes(TreeNode root, int maxValue){
        if (root == null)return 0;
        int newMaxValue = Math.max(root.val, maxValue);
        int left_numGoodNodes = 0;
        int right_numGoodNodes = 0;
        if(root.left != null)
            left_numGoodNodes = this.numGoodNodes(root.left, newMaxValue);
        if(root.right != null)
            right_numGoodNodes = this.numGoodNodes(root.right, newMaxValue);
        if(root.val >= maxValue)
            return left_numGoodNodes + right_numGoodNodes + 1;
        return left_numGoodNodes + right_numGoodNodes;
    }
}