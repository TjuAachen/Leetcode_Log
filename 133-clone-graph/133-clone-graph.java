/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        //@input : one node denoting a connected graph
        // in a node, there is a value and a adjacency list for neighbors
        //@output : a cloned graph
        //@edge case : no
        //@breaking down:
        // 1. bfs, if not copy, create the copy of this node and add into the copied values;
        // 2. traverse the adjacency list and if uncopied, then create a copy and add into the adjacency list; if copied, then add copied node into the adjacency list.
       //3. add the node into the queue
        // 4. repeat the process until queue is empty
        LinkedList<Node> queue = new LinkedList<>();
        Map<Node, Node> copyToOriginal = new HashMap<>();
        Map<Node, Node> originalToCopy = new HashMap<>();
        if(node == null)return null;
        Node root = new Node(node.val);
        originalToCopy.put(node, root);
        copyToOriginal.put(root, node);
        queue.addLast(root);
        Set<Node> visited = new HashSet<>();
        visited.add(root);
        //bfs，注意不要重复
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                Node popped = queue.pollFirst();
                Node poppedOriginal = copyToOriginal.get(popped);
                for(Node neighbor: poppedOriginal.neighbors){
                    if(!originalToCopy.containsKey(neighbor)){
                        Node copiedNeighbor = new Node(neighbor.val);
                        originalToCopy.put(neighbor, copiedNeighbor);
                        copyToOriginal.put(copiedNeighbor, neighbor);
                    }
                    if(!visited.contains(originalToCopy.get(neighbor))){
                        queue.addLast(originalToCopy.get(neighbor));
                        visited.add(originalToCopy.get(neighbor));
                    }
                    popped.neighbors.add(originalToCopy.get(neighbor));
                }
                
            }
            
        }
        //System.out.println(node.val);
        return root;
        
        
        
        
        
    }
}