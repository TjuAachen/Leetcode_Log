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
    public String tree2str(TreeNode root) {
        if(root == null)return "()";
        String left = tree2str(root.left);
        String right = tree2str(root.right);
        if(!right.equals("()")){
        if(left.equals("()")){
        return Integer.toString(root.val) + left +"(" +right + ")";
        }else{
            return Integer.toString(root.val) + "("+left +")"+"(" +right + ")";
        }
        }else if(!left.equals("()")){
            return Integer.toString(root.val) +"("+ left + ")";
        }
        return Integer.toString(root.val); 
    }
}