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
    public ListNode partition(ListNode head, int x) {
        ListNode dumb = new ListNode(0);
        ListNode small = dumb;
        ListNode noSmallDumb = new ListNode(0);
        ListNode noSmall = noSmallDumb;
        ListNode  cur = head;
        ListNode nxt;
        while(cur != null){
            nxt = cur.next;
            if(cur.val < x){
                small.next = cur;
                cur.next = null;
                small = small.next;
            }else{
                noSmall.next = cur;
                cur.next = null;
                noSmall = noSmall.next;
            }
            cur = nxt;
        }
        small.next = noSmallDumb.next;
        return dumb.next;
    }
}