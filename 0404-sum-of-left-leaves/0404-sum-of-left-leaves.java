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
        LinkedList<TreeNode> stack = new LinkedList<>();
        //pre-order iterative
        TreeNode cur = root;
        
        int res = 0;
        
        while(!stack.isEmpty() || cur != null){
            
            while(cur != null){
                stack.addLast(cur);
                cur = cur.left;
                if(cur != null && cur.left == null && cur.right == null)
                    res += cur.val;
            }
            
            TreeNode popped = stack.pollLast();
            cur = popped.right;
            
        }
        
        return res;
        
        
        
        
        
    }
}