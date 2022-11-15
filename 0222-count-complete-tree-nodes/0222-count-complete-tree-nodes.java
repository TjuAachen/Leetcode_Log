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
    public int countNodes(TreeNode root) {
        
        int maximumDepth = computeDepth(root);
        
        int left = 0;
        int right = (1<< maximumDepth) - 1;
        
        int prevNodes = right;
        
       // System.out.println(maximumDepth);
        
        
        while(left <= right){
            
            int mid = left + (right - left) / 2;
         //   System.out.println(mid);
            if(check(mid, maximumDepth, root)){
                if(right == mid || !check(mid + 1, maximumDepth, root))
                    return prevNodes + mid + 1;
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        
        return prevNodes;
        
        
    }
    
    public boolean check(int idx, int maximumDepth, TreeNode root){
        TreeNode node = root;
        for(int d = maximumDepth - 1; d > -1; d--){
            int mask = (1<<d);
            int curBit = idx&mask;
            
            if(node == null)
                return false;
            if(curBit != 0){
                node = node.right;
            }else{
                node = node.left;
            }
            
        }
        
        return node != null;
    }
    
    public int computeDepth(TreeNode root){
        
        int depth = 0;
        TreeNode node = root;
        
        while(node != null && node.left != null){
            depth++;
            node = node.left;
        }
        
        return depth;
    }
    
}