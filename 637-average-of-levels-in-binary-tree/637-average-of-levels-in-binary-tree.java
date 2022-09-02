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
    public List<Double> averageOfLevels(TreeNode root) {
        //level order traversal
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.addLast(root);
        List<Double> res = new LinkedList<>();
        while(!queue.isEmpty()){
            int size = queue.size();
            long curLevelSum = 0;
            for(int i = 0; i < size; i++){
                TreeNode temp = queue.pollFirst();
                curLevelSum += temp.val;
                if (temp.left != null)queue.addLast(temp.left);
                if (temp.right != null) queue.addLast(temp.right);
            }
            res.add((double)curLevelSum/size);
            
        }
        return res;
    }
}