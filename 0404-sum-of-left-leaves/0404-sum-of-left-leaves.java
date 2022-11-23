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
    int res = 0;
    public int sumOfLeftLeaves(TreeNode root) {
        TreeNode cur = root;
        
        while(cur != null){
            if(cur.left != null){
                TreeNode node = getRightMostNodeOfLeftSubtree(cur);
                node.right = cur.right;
                cur = cur.left;
                if(cur != null && cur.left == null && cur.right == node.right)
                    res += cur.val;
            }else{
                cur = cur.right;
            }
        }
        
        return res;
        
    }
    
    public TreeNode getRightMostNodeOfLeftSubtree(TreeNode cur){
        
        cur = cur.left;
        
        while(cur.right != null){
            cur = cur.right;
        }
        
        return cur;
        
        
    }
}