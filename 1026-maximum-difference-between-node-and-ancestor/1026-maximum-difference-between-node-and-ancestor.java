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
    int result = 0;
    public int maxAncestorDiff(TreeNode root) {

        minAndMax(root);
        
        return result;
        
    }
    
    public int[] minAndMax(TreeNode root){
        if (root.left == null && root.right == null)
            return new int[]{root.val, root.val};
        int[] ansLeft = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
        int[] ansRight = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
        
        if (root.left != null)
            ansLeft = minAndMax(root.left);
        if (root.right != null)
            ansRight = minAndMax(root.right);
        int[] ans = new int[]{Math.min(ansLeft[0], ansRight[0]), Math.max(ansLeft[1], ansRight[1])};
        
        
        int temp = Math.max(Math.abs(ans[0] - root.val), Math.abs(ans[1] - root.val));
        result = Math.max(temp, result);
        
        
        ans[0] = Math.min(ans[0], root.val);
        ans[1] = Math.max(ans[1], root.val);
        
        
        
        return ans;
        
    }
    
}