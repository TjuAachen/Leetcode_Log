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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dumb = new ListNode();
        int count = 1;
        ListNode p = dumb;
        ListNode newTail = null;
        ListNode cur = head;
        ListNode nxt;
        while(cur != null){
            nxt = cur.next;
            if(count < left){
                p.next = cur;
                cur.next = null;
                p = p.next;
            }else if(count >= left && count <= right){
                ListNode following = p.next;
                p.next = cur;
                cur.next = following;
            }else if (count == right + 1){
                p = newTail;
                p.next = cur;
                cur.next = null;
                p = p.next;
            }else{
                p.next = cur;
                cur.next = null;
                p = p.next;
            }
            if(count == left){
                newTail = cur;
            }
            cur = nxt;
            count++;
        }
        return dumb.next;
        
    }
}