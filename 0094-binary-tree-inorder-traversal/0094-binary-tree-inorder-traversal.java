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
    public List<Integer> inorderTraversal(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        List<Integer> ans = new LinkedList<>();
        TreeNode cur = root;
        
        while(cur != null ||!stack.isEmpty()) {
            while(cur != null) {
                stack.addLast(cur);
                cur = cur.left;
            }
            
            TreeNode leftMost = stack.pollLast();
            ans.add(leftMost.val);
            cur = leftMost.right;
        }
        
        return ans;
        
    }
}