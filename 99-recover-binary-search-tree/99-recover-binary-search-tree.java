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
    public void recoverTree(TreeNode root) {
        TreeNode prev = null;
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;
        TreeNode first = null, second = null;
        while(!stack.isEmpty() || cur != null){
            while(cur!=null){
                stack.addLast(cur);
                cur = cur.left;
            }
            TreeNode popped = stack.pollLast();
            if(prev != null && prev.val > popped.val && first == null){
                first = prev;
            }
            if(prev != null && prev.val > popped.val){
                second = popped;
            }
            prev = popped;
            cur = popped.right;
        }
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
     //  return root;
    }
}