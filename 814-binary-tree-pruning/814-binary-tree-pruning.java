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
    public TreeNode pruneTree(TreeNode root) {
        TreeNode dumb =new TreeNode(1);
        dumb.left = root;
        TreeNode res = prune(dumb);
        return dumb.left;
        
    }
    //true 
    public TreeNode prune(TreeNode root){
        if(root == null)return null;
        TreeNode left = prune(root.left);
        TreeNode right = prune(root.right);
        if(root.val == 0 && left == null && right == null)return null;
        root.left = left;
        root.right = right;
        return root;
    }
}