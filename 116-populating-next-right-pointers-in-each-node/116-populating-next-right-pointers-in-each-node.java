/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        //@input: a perfect binary tree
        //@output: the head with next pointer 
        //bfs, start from the leftmost node in the level one up.
        //then set the next pointer of the node's left children to the node's right children
        //set the next pointer of the node's right children to the next node's left
        //@edge case: the root is null
        
        Node prev = root;
        while(prev != null){
            connectNextLevel(prev);
            prev = prev.left;
        }
        return root;
    }
    public void connectNextLevel(Node root){
        Node cur = root;
        while(cur != null && cur.left != null){
            cur.left.next = cur.right;
            if(cur.next != null){
                cur.right.next = cur.next.left;
            }
            cur = cur.next;
        }
    }
}