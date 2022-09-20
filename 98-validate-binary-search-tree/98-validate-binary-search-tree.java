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
    public boolean isValidBST(TreeNode root) {
        int prev = Integer.MIN_VALUE;
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;
        int count = 0;
        while(!stack.isEmpty() || cur != null){
            while(cur!=null){
                stack.addLast(cur);
                cur = cur.left;
            }
            TreeNode popped = stack.pollLast();
            if(popped.val < prev)return false;
            if(prev == popped.val && prev != Integer.MIN_VALUE)return false;
            if(prev == popped.val && prev == Integer.MIN_VALUE && count > 0)return false;
            prev = popped.val;
            cur = popped.right;
            count += 1;
            
        }
        return true;
        
        
    }
}