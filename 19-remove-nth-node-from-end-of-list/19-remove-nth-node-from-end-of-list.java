/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dumb = new ListNode();
        dumb.next = head;
        ListNode prevRemovedNode = findNodeByIdx(dumb, n);
        prevRemovedNode.next = prevRemovedNode.next.next;
        return dumb.next;

    }
    public ListNode findNodeByIdx(ListNode dumb, int n){
        ListNode head = dumb.next;
        ListNode fast = head, slow = dumb;
        //move n first
        int i = 0;
        while(fast != null && i < n){
            fast = fast.next;
            i++;   
        }
        while(fast != null){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}