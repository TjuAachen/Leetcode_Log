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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dumb = new ListNode();
        dumb.next = head;
        ListNode prev = dumb;
        ListNode cur = head;
        
        while(cur != null){
            ListNode nxt = cur;
            int countDuplicate = 0;
            ListNode curPrev = prev;
            while(nxt != null && nxt.val == cur.val){
                curPrev = nxt;
                nxt = nxt.next;
                countDuplicate++;
            }
            cur = nxt;
            if(countDuplicate > 1){
                curPrev.next = null;
                prev.next = cur;
            }else{
                prev = curPrev;
            }
        }
        return dumb.next;
        
    }
}