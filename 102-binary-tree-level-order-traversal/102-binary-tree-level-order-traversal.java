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
    public List<List<Integer>> levelOrder(TreeNode root) {
        LinkedList<TreeNode> queue = new LinkedList<>();
        if(root != null)queue.add(root);
        List<List<Integer>> res = new LinkedList<>();
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> temp = new LinkedList<>();
            for(int i = 0; i < size; i++){
                TreeNode popped = queue.pollFirst();
                temp.add(popped.val);
                if(popped.left != null){
                    queue.add(popped.left);
                }
                if(popped.right != null){
                    queue.add(popped.right);
                }
            }
            res.add(temp);
        }
        return res;
        
        
    }
}