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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<TreeNode> queue = new LinkedList<>();
        LinkedList<List<Integer>> res = new LinkedList<>();
        if(root == null)return new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            int size = queue.size();
            LinkedList<Integer> temp = new LinkedList<>();
            for(int i = 0; i < size; i++){
                TreeNode popped = queue.pollFirst();
                if(popped.left != null)queue.addLast(popped.left);
                if(popped.right != null)queue.addLast(popped.right);
                temp.addLast(popped.val);
            }
            res.addFirst((LinkedList) temp.clone());
        }
        return res;
        
        
        
        
    }
}