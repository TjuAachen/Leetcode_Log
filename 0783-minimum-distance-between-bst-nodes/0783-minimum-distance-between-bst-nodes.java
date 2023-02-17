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
    public int minDiffInBST(TreeNode root) {
        //middle-order traversal
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;
        int res = Integer.MAX_VALUE;
        TreeNode prev = null;
        
        while (!stack.isEmpty() || cur != null) {
            while (cur != null) {
                stack.add(cur);
                cur = cur.left;
            }
            cur = stack.pollLast();
            if (prev != null)
                res = Math.min(res, cur.val - prev.val);
            prev = cur;
            cur = cur.right;
            
        }
        
        return res;
    }
}