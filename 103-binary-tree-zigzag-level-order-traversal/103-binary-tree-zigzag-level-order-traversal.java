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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        LinkedList<TreeNode> queue = new LinkedList<>();
        if(root != null){
            queue.add(root);
        }
        List<List<Integer>> res = new LinkedList<>();
        boolean isOrderLeft = true;
        
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> temp = new LinkedList<>();
            for(int i = 0; i < size; i++){
                if(isOrderLeft){
                    TreeNode popped = queue.pollFirst();
                    temp.add(popped.val);
                if(popped.left != null){
                    queue.addLast(popped.left);
                }
                if(popped.right != null){
                    queue.addLast(popped.right);
                }
                                       
                }else{
                    TreeNode popped = queue.pollLast();
                    temp.add(popped.val);
                    if(popped.right != null){
                        queue.addFirst(popped.right);
                    }
                    if(popped.left != null){
                        queue.addFirst(popped.left);
                    }
                }

            }
            res.add(temp);
            isOrderLeft = !isOrderLeft;
        }
        return res;
        
        
        
    }
}