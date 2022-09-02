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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dumb = new ListNode(0);
        dumb.next = head;
        ListNode p = head;
        int count = 1;
        ListNode res = new ListNode(0);
        ListNode resP = res;
        while(p != null){
            if(count != 0 && count%k == 0){
                //extract the k list
                ListNode nxt = p.next;
                p.next = null;
                ListNode newTail = dumb.next;
                resP.next = this.reverseList(newTail);
                dumb.next = nxt;
                resP = newTail;
                p = dumb.next;
            }else{
                p = p.next;
            }
            count++;
        }
        if(dumb.next != null){
            resP.next =dumb.next;
        }
        return res.next;
    }
    public ListNode reverseList(ListNode head){
        ListNode cur = head;
        ListNode prev = null;
        while(cur != null){
            ListNode nxt = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nxt;
        }
        return prev;
        
        
        
        
        
        
    }
}