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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        int nullNum = 0;
        if (p == null)
            nullNum++;
        if (q == null)
            nullNum++;
        
        if (nullNum == 2)
            return true;
        if (nullNum == 1)
            return false;
        if (p.val != q.val)
            return false;
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);     
    }
}