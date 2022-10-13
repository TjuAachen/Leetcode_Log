/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head == null)return null;
        //如何照顾边边角角
        ListNode fast = getIntersect(head);
        if(fast == null)return null;
        ListNode slow = head;
        while(slow != fast){
            slow = slow.next;
            fast = fast.next;
        }
        return fast;

    }
    public ListNode getIntersect(ListNode head){
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                return slow;
            }
        }
        return null;
    }
}