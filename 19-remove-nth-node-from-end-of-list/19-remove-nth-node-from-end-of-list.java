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
        ListNode dumb = new ListNode(0, head);
        ListNode first = head;
        ListNode second = dumb;
        //first goes first n
        int count = 0;
        while(first != null){
            first = first.next;
            if (count > n - 1){
                second = second.next;
            }
            count += 1;
        }
        // delete the node
        second.next = second.next.next;
        return dumb.next;
    }
}