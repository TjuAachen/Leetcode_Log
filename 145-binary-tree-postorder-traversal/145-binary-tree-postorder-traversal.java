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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;
        TreeNode prev = null;
        while(cur != null || !stack.isEmpty()){
            while(cur != null){
                stack.addLast(cur);
                cur = cur.left;
            }
            
            TreeNode top = stack.peekLast();
            if(top.right == null || prev == top.right){
                prev = stack.pollLast();
                res.add(prev.val);
            }else{
                cur = top.right;
            }
        }
        return res;
    }
}