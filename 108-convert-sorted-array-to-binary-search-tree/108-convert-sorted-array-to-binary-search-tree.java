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
    public TreeNode sortedArrayToBST(int[] nums) {
        int mid = nums.length / 2;
        if(nums.length == 0)return null;
        TreeNode leftSubTree = sortedArrayToBST(Arrays.copyOfRange(nums, 0, mid));
        TreeNode rightSubTree = sortedArrayToBST(Arrays.copyOfRange(nums, mid + 1, nums.length));
        TreeNode root = new TreeNode(nums[mid]);
        root.left = leftSubTree;
        root.right = rightSubTree;
        return root;
    }
}