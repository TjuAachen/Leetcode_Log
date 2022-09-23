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
        //input: the root of a non-perfect binary tree
        //output: tree with populated next pointer
        //1. find the head of the nodes in the upper level
        //2.go to the next non-null node not equal to cur
        //3.link the cur to the next, go the next and repeat the same process above
        Node prev = root;
        
        while(prev != null){
            Node prevCur = prev;
            Node cur = null;
            Node nxtHead = null;
            while(prevCur != null){
                List<Node> temp = findprevNext(prevCur, cur, nxtHead);
                prevCur = temp.get(0);
                cur = temp.get(1);
                nxtHead = temp.get(2);
            }
            prev = nxtHead;
        }
        return root;
        
        
        
        
        
    }
    public List<Node> findprevNext(Node prevCur, Node cur, Node nxtHead){
        while(prevCur != null){
            if(prevCur.left != null && prevCur.left != cur){
                if(cur != null){
                cur.next = prevCur.left;
                cur = cur.next;
                }else{
                    cur = prevCur.left;
                    nxtHead = cur;
                }
                break;
            }
            if(prevCur.right != null && prevCur.right != cur){
                if(cur != null){
                    cur.next = prevCur.right;
                    cur = cur.next;
                }else{
                    cur = prevCur.right;
                    nxtHead = cur;
                }
                prevCur = prevCur.next;
                break;
            }
            prevCur = prevCur.next;
        }
        List<Node> res = new LinkedList<>();
        res.add(prevCur);
        res.add(cur);
        res.add(nxtHead);
        return res;
    }
        
}