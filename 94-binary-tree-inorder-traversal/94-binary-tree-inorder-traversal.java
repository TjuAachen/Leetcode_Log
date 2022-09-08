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
        //morris inorder
        TreeNode cur = root;
        List<Integer> res = new LinkedList<>();
        while(cur != null){
            if(cur.left == null){
                res.add(cur.val);
                cur = cur.right;
                continue;
            }
            TreeNode prev = cur.left;
            while(prev.right != null && prev.right != cur){
                prev = prev.right;
            }
            if(prev.right == null){
                prev.right = cur;
                cur = cur.left;
            }else{
                res.add(cur.val);
                prev.right = null;
                cur = cur.right;
            }
        }
        return res;
    }
}