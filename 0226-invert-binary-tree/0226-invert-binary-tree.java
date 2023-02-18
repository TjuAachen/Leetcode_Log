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
    public TreeNode invertTree(TreeNode root) {
        if (root == null)
            return root;
        invert(root, root, root.left, root.right);
        return root;
    }
    
    public void invert(TreeNode leftPrev, TreeNode rightPrev,TreeNode left, TreeNode right) {
        if (left == null && right == null)
            return;
        if (left != null && right == null) {
            rightPrev.right = left;
            leftPrev.left = null;
            invert(left, left, left.left, left.right);
            return;
        }
        if (left == null && right != null) {
            leftPrev.left = right;
            rightPrev.right = null;
            invert(right, right, right.left, right.right);
            return;
        }
        int temp = left.val;
        left.val = right.val;
        right.val = temp;
        invert(left, right, left.left, right.right);
        invert(right, left, right.left, left.right);
        return;
    }
    
}