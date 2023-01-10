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
    public boolean check(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;
        if (p == null || q == null)
            return false;
        return p.val == q.val;
    }
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        LinkedList<TreeNode> queueP = new LinkedList<>();
        LinkedList<TreeNode> queueQ = new LinkedList<>();
        queueP.addLast(p);
        queueQ.addLast(q);
        
        while (!queueP.isEmpty() && !queueQ.isEmpty()) {
            TreeNode poppedP = queueP.pollFirst(), poppedQ = queueQ.pollFirst();
            if (!check(poppedP, poppedQ)) {
                return false;
            }
            
            if (!nxt(poppedP, poppedQ, queueP, queueQ))
                return false;        
        }
        
        if (!queueP.isEmpty() || !queueQ.isEmpty())
            return false;
        return true;
        
  
    }
    
    public boolean nxt(TreeNode poppedP, TreeNode poppedQ, LinkedList<TreeNode> queueP, LinkedList<TreeNode> queueQ) {
        if (poppedP == null && poppedQ == null)
            return true;
        if (poppedP.left != null && poppedQ.left != null) {
            queueP.addLast(poppedP.left);
            queueQ.addLast(poppedQ.left);
        } else if (poppedP.left != null || poppedQ.left != null)
            return false;
        if (poppedP.right != null && poppedQ.right != null) {
            queueP.addLast(poppedP.right);
            queueQ.addLast(poppedQ.right);
        } else if (poppedP.right != null || poppedQ.right != null)
            return false;        
        return true;
    }
    
}