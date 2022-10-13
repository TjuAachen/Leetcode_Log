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
        TreeNode curNode = root;
        List<Integer> res = new LinkedList<>();
        while(!stack.isEmpty() || curNode != null){
            while(curNode != null){
                res.add(curNode.val);
                stack.add(curNode);
                curNode = curNode.left;
            }
            TreeNode popped = stack.pollLast();
            curNode = popped.right;
        }
        return res;
        
        
    }
}