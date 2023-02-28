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
    Map<String, List<TreeNode>> subtrees = new HashMap<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        //take out all subtrees
        findSubtrees(root);
        List<TreeNode> res = new LinkedList<>();
        for (Map.Entry<String, List<TreeNode>> entry : subtrees.entrySet()) {
            List<TreeNode> cur = entry.getValue();
            if (cur.size() > 1) {
                res.add(cur.get(0));
            }
        }
        
        return res;
        
        
    }
    
    public String findSubtrees(TreeNode root) {
        if (root == null)
            return "null";
        String val = ((Integer) root.val).toString();
        String left = findSubtrees(root.left);
        String right = findSubtrees(root.right);
        String curSub = val + "#" + left + "#" + right;
        subtrees.computeIfAbsent(curSub, k -> new LinkedList<TreeNode>());
        subtrees.get(curSub).add(root);
        
        return curSub;
    }
    
    
}