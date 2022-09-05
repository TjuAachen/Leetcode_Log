/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        LinkedList<Node> queue = new LinkedList<>();
        List<List<Integer>> res = new LinkedList<>();
        if(root == null)return res;
        
        queue.addLast(root);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> temp = new LinkedList<>();
            for(int i = 0; i < size; i++){
                Node popped = queue.pollFirst();
                temp.add(popped.val);
                for(Node j : popped.children){
                    
                    queue.addLast(j);
                }
            
            }
            res.add(temp);
        }
        return res;
    }
}