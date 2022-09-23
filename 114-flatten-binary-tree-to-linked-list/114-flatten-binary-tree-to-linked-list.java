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
    public void flatten(TreeNode root) {
        //@input a binary tree
        //@output linked list with the same treenode class, right is same to the next and it is a pre-order traversal.
        //morris pre-order traversal
        //@edge case 
        TreeNode dumb = new TreeNode(0);
        TreeNode cur = root;
        TreeNode pointer = dumb;
        while(cur != null){
            pointer.right = cur;
            pointer = cur;
            if(cur.left != null){
                TreeNode node = getRightMostNode(cur);
                node.right = cur.right;
                cur.right = null;
                TreeNode prev = cur;
                cur = cur.left;
                prev.left = null;
                
            }else{
                cur = cur.right;
            }
        }
        
        
        
        
        
    }
    public TreeNode getRightMostNode(TreeNode cur){
        TreeNode node = cur.left;
        while(node.right != null){
            node = node.right;
        }
        return node;
    }
    
}