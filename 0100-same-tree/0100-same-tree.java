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

    public boolean isSameTree(TreeNode p, TreeNode q) {
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.addLast(p);
        queue.addLast(q);
        
        while (!queue.isEmpty()) {
            TreeNode popped1 = queue.pollFirst(), popped2 = queue.pollFirst();
            if (popped1 == null && popped2 == null)
                continue;
            if (popped1 == null || popped2 == null)
                return false;
            if (popped1.val != popped2.val)
                return false;
            queue.addLast(popped1.left);
            queue.addLast(popped2.left);
            queue.addLast(popped1.right);
            queue.addLast(popped2.right);
        }
        
        return true;
        

  
    }
    
    
}