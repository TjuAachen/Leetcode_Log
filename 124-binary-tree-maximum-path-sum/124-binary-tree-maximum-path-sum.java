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
    int maxRes = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        processRoot(root);
        return maxRes;
    }
    public int processRoot(TreeNode root){
        if(root.left == null && root.right == null){
            maxRes = Math.max(maxRes, root.val);
            return root.val;
        }
        int left = 0, right = 0;
        if(root.left != null){
            left = Math.max(left,processRoot(root.left));
        }
        if(root.right != null){
            right = Math.max(right,processRoot(root.right));
        }
       // System.out.printf("%d %d %d\n",left, right, root.val);
        maxRes = Math.max(maxRes, left + root.val + right);
        return Math.max(left, right) + root.val;    
    }
}