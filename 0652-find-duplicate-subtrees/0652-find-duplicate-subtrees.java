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
    Map<Integer, List<TreeNode>> subtrees = new HashMap<>();
    Map<String, Integer> tripletID = new HashMap<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        //take out all subtrees
        findSubtrees(root);
        List<TreeNode> res = new LinkedList<>();
        for (Map.Entry<Integer, List<TreeNode>> entry : subtrees.entrySet()) {
            List<TreeNode> cur = entry.getValue();
            if (cur.size() > 1) {
                res.add(cur.get(0));
            }
        }
        
        return res;
        
        
    }
    
    public int findSubtrees(TreeNode root) {
        if (root == null)
            return 0;
        String triplet = findSubtrees(root.left) + "," + root.val + "," + findSubtrees(root.right);
        
        if (!tripletID.containsKey(triplet)) {
            tripletID.put(triplet, tripletID.size() + 1);
        }
        int id = tripletID.get(triplet);

        subtrees.computeIfAbsent(id, k -> new LinkedList<TreeNode>());
        subtrees.get(id).add(root);
        
        return id;
    }
    
    
}