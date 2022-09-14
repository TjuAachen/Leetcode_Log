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
    int[] numFreq = new int[10];
    int count = 0;
    public int pseudoPalindromicPaths (TreeNode root) {
        if(root.left == null && root.right == null){
            numFreq[root.val]+=1;
            if(isPalindromic(numFreq))count++;
            numFreq[root.val]-=1;
            return count;
        }
        numFreq[root.val]+=1;
        if (root.left != null)pseudoPalindromicPaths(root.left);
        if(root.right != null)pseudoPalindromicPaths(root.right);
        numFreq[root.val]-=1;
        return count;
    }
    public boolean isPalindromic(int[] numFreq){
        int numOdd = 0;
        for(int i = 1; i < 10; i++){
            if(numFreq[i]%2 == 1){
                numOdd++;
            }
            if(numOdd > 1)return false;
        }
        return true;
        
        
        
    }
    
}