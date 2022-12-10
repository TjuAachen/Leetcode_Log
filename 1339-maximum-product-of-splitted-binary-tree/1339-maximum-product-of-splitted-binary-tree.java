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
    
    int totalSum = 0;
    Map<TreeNode, Integer> nodeSum = new HashMap<>();
    long MOD = (long)1000000007;
    public int maxProduct(TreeNode root) {
        rootSum(root);
        
        long res = (long) 0;
        
        for (Map.Entry<TreeNode, Integer> entry : nodeSum.entrySet()){
            int oneSum = entry.getValue();
            int anotherSum = totalSum - oneSum;
            
            res = Math.max(res, (long) oneSum * (long) anotherSum);
         //   System.out.printf("%d %d %d\n", oneSum, anotherSum, (long) oneSum * (long) anotherSum);
        }
        
        return (int) (res%MOD);
        
        
        
    }
    
    public int rootSum(TreeNode root){
        if (root.left == null && root.right == null){
            nodeSum.put(root, root.val);
            totalSum += root.val;
            return root.val;
        }
        totalSum += root.val;
        int left = 0;
        int right = 0;
        if (root.left != null){
            left = rootSum(root.left);
        }
        if (root.right != null){
            right = rootSum(root.right);
        }
        
        nodeSum.put(root, root.val + left + right);
        
        return left + right + root.val;
    }
    
    
    
    
}