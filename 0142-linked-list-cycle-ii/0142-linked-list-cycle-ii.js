/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    if (head == null)
        return null;

    var doubleNode = head;
    var singleNode = head;
    
    while (doubleNode.next != null && doubleNode.next.next != null) {
        doubleNode = doubleNode.next.next;
        singleNode = singleNode.next;
        if (singleNode == doubleNode)
            break;
    }
    
    if (doubleNode.next != null && doubleNode.next.next != null && singleNode == doubleNode) {
        singleNode = head;
        var i = 0;
        while (doubleNode != singleNode) {
            doubleNode = doubleNode.next;
            singleNode = singleNode.next;
            i++;
        }
        return singleNode;
    }else {
        return null;
    }
    
    
};