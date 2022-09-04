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
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        Map<Integer, Map<Integer,List<Integer>>> posToValues = new TreeMap<>();
        //preorder traversal to find the column values
        preorderTraversal(root, 0, 0, posToValues);
        
        List<List<Integer>> res = new LinkedList<>();
        for (Map.Entry<Integer, Map<Integer,List<Integer>>>
                 entry : posToValues.entrySet()){
            int col = entry.getKey();
            Map<Integer,List<Integer>> rowToVal = entry.getValue();
            List<Integer> temp_res = new LinkedList<>();
            
            for(Map.Entry<Integer, List<Integer>> entry2 : rowToVal.entrySet()){
                int row = entry2.getKey();
                List<Integer> nodeVal = entry2.getValue();
                
                Collections.sort(nodeVal);
                temp_res.addAll(nodeVal);
            }
            res.add(temp_res);
        }
        return res;
        
    }
    public void preorderTraversal(TreeNode root, int row, int col, Map<Integer, Map<Integer,List<Integer>>> posToValues){
        if(root == null)return;
        
        posToValues.computeIfAbsent(col, k -> new TreeMap<>());
        Map<Integer,List<Integer>> rowToValues = posToValues.get(col);
        rowToValues.computeIfAbsent(row, k -> new LinkedList<>());
        List<Integer> values = rowToValues.get(row);
        values.add(root.val);
        //left
        preorderTraversal(root.left, row + 1, col - 1, posToValues);
        //right
        preorderTraversal(root.right, row + 1, col + 1, posToValues);
        
        return;
        
    }
}