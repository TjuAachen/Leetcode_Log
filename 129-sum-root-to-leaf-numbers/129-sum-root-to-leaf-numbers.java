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
    int res = 0;
    int sum = 0;
    public int sumNumbers(TreeNode root) {
        //@input : root of a tree
        //@output : the sum of all root-to-leaf numbers
        //edge case : null
        //breaking down:
        //1.pre-order traversal to find the corresponding number for each root
        //when a leaf is reached, the result is added into the sum
        if(root.left == null && root.right == null){
            sum = sum * 10 + root.val;
            res += sum;
            sum = (sum - root.val) / 10;
            return res;
        }
        sum = sum * 10 + root.val;
        if(root.left != null){
            sumNumbers(root.left);
        }
        if(root.right != null){
            sumNumbers(root.right);
        }
        sum = (sum - root.val) / 10;
        return res;
    }
}