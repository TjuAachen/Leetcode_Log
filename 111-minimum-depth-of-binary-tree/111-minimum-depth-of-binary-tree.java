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
    public int minDepth(TreeNode root) {
        //@input root of a binary tree
        //@output the minimum depth the number of nodes from root down to the nearest leaf
        //bfs/dfs
        LinkedList<TreeNode> queue = new LinkedList<>();
        if(root == null)return 0;
        queue.addLast(root);
        int minDepth = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            minDepth += 1;
            for(int i = 0; i < size; i++){
                TreeNode popped = queue.pollFirst();
                if(popped.left == null && popped.right == null){
                    return minDepth;
                }
                if(popped.left != null){
                    queue.addLast(popped.left);
                }
                if(popped.right != null){
                    queue.addLast(popped.right);
                }
                
            }
        }
        return minDepth;
        
        
        
    }
}