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
    public List<Integer> preorderTraversal(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;
        List<Integer> ans = new LinkedList<>();
        
        while(!stack.isEmpty() || cur != null) {
            while(cur != null) {
                ans.add(cur.val);
                stack.addLast(cur);
                cur = cur.left;
            }
            cur = stack.pollLast();
            cur = cur.right;
            
        }
        
        return ans;
        
    }
}