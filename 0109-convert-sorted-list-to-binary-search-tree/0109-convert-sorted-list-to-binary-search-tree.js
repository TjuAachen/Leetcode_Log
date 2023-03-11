/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    // move to the middle - 1
    
    // set middle - 1 as left; middle as root; middle + 1 as the right
    // repeat the process above
    //(x ^ (n - 2) + y ^ (n - 2)) * xy = x ^ (n - 1) * y + x * y ^ (n - 1)
    // (x ^ (n - 1) + y ^ (n - 1)) * (x + y) = x^n + y^n + x^(n-1) * y + x * y^(n-1)
    //f(n - 1) * (x + y) - f(n - 2) * xy = x ^ n + y ^ n
    if (head == null) {
        return null;
    }
    
    if (head.next == null) {
        return new TreeNode(head.val);
    }
    
    //fast/slow pointer to move to middle -1
    var slow = head;
    var fast = head.next.next;
    
    while (fast != null && fast.next != null) {
        fast = fast.next.next;
        slow = slow.next;
    }
    // left node
    var rootNodeVal = slow.next.val;
    var rightListNode = slow.next.next;
    slow.next = null;
    var leftNode = arguments.callee(head);
    var rightNode = arguments.callee(rightListNode);
    //root node
    var rootNode = new TreeNode(rootNodeVal, leftNode, rightNode);
    
    return rootNode;

    
};