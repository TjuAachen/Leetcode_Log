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

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> pathsList = new ArrayList<List<Integer>>();
        List<Integer> pathNodes = new ArrayList<Integer>();
        recurseTree(root, targetSum, pathNodes, pathsList);
        return pathsList;
        
        
        
    }
    
    private void recurseTree(TreeNode node, int remainingSum, List<Integer> pathNodes, List<List<Integer>> pathsList){
        if(node == null)return;
        pathNodes.add(node.val);
        //check if the current node is a leaf and also if it equals our remaining sum. If it does, add the path to our list of paths.
        if(remainingSum == node.val && node.left == null && node.right == null){
            pathsList.add(new ArrayList<>(pathNodes));
        }else{
            recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList);
            recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList);
        }
        pathNodes.remove(pathNodes.size() - 1);
    }
}