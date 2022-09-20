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
    public List<TreeNode> generateTrees(int n) {
        return generateSubTree(1, n);
    }
    public List<TreeNode> generateSubTree(int start, int end){
        List<TreeNode> res = new LinkedList<>();
        if(start > end){
            res.add(null);
            return res;
        }
        for(int i = start; i < end + 1; i++){
            List<TreeNode> leftTrees = generateSubTree(start, i-1);
            List<TreeNode> rightTrees = generateSubTree(i+1, end);
            for(TreeNode leftTree : leftTrees)
                for(TreeNode rightTree : rightTrees){
                    TreeNode root = new TreeNode(i);
                    root.left = leftTree;
                    root.right = rightTree;
                    res.add(root);
                }
        }
        return res;
    }
    

    
    
}