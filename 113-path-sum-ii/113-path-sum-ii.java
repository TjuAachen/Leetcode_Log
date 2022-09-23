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
    private LinkedList<Integer> temp = new LinkedList<>();
    private List<List<Integer>> res = new LinkedList<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        //@input: the root of a binary tree
        //@output a list of the node values sum equal to targetSum
        //@edge case
        //1.recursive/backtracking, select the cur root and change the target sum
        //add cur root to the temp
        //2.if leaf is reached and target sum == 0, add temp to the res
        if(root == null)return res;
        if(root.left == null && root.right == null && targetSum == root.val){
            temp.addLast(root.val);
            res.add((List)temp.clone());
            temp.pollLast();
            return res;
        }
        temp.add(root.val);
        pathSum(root.left, targetSum - root.val);
        temp.pollLast();
        temp.add(root.val);
        pathSum(root.right, targetSum - root.val);
        temp.pollLast();
        return res;
    }
}