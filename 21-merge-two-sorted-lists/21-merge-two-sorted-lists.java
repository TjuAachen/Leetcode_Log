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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dumb = new ListNode(0);
        ListNode p1 = list1;
        ListNode p2 = list2;
        ListNode q = dumb;
        while(p1 != null || p2 != null){
            int p1Val = 101, p2Val = 101;
            if(p1 != null){
                p1Val = p1.val;
            }
            if(p2 != null){
                p2Val = p2.val;
            }
            ListNode add = new ListNode(Math.min(p1Val, p2Val));
            q.next = add;
            q = q.next;
            if(p1Val == add.val){
                p1 = p1.next;
            }else{
                p2 = p2.next;
            }
            
        }
        return dumb.next;
        
        
        
    }
}