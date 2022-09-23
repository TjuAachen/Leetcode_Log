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
    Node leftMost;
    Node prev;
    public Node connect(Node root) {
        //input: the root of a non-perfect binary tree
        //output: tree with populated next pointer
        //while(leftMost != null)
        //1.cur = leftMost
        //prev = null
        //2.process leftMost.left, leftMost.right
        //set the leftMost for the next level
        leftMost = root;
        while(leftMost != null){
            Node cur = leftMost;
            prev = null;
            leftMost = null;
            while(cur != null){
                processChild(cur.left);
                processChild(cur.right);
                cur = cur.next;
            }
        }
        return root;
    }
    public void processChild(Node childNode){
        if(childNode == null)return;
        if(prev == null){
            prev = childNode;
            leftMost = childNode;
        }else{
            prev.next = childNode;
            prev = prev.next;
        }
    }

        
}