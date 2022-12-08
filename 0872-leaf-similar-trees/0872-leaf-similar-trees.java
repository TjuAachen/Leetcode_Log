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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> root1Leaves = new ArrayList<Integer>();
        ArrayList<Integer> root2Leaves = new ArrayList<Integer>();
        
        extractLeaves(root1, root1Leaves);
        extractLeaves(root2, root2Leaves);
        
        return isEqual(root1Leaves, root2Leaves);
        
        
        
    }
    
    public void extractLeaves(TreeNode root, ArrayList<Integer> leaves){
        
        if (root.left == null && root.right == null){
            leaves.add(root.val);
            return;
        }
        if(root.left != null)
            extractLeaves(root.left, leaves);
        if(root.right != null)
            extractLeaves(root.right, leaves);
        return;
    }
    
    public boolean isEqual(ArrayList<Integer> leaves1, ArrayList<Integer> leaves2){
        if(leaves1.size() != leaves2.size())
            return false;
        for (int i = 0; i < leaves1.size(); i++){
            if (leaves1.get(i) != leaves2.get(i))
                return false;
        }
        return true;
    }
}