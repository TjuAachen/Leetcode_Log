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
    public ListNode rotateRight(ListNode head, int k) {
        //calculate the length of list
        int listLen = 0;
        ListNode node = head;
        ListNode tail = head;
        if(head == null)return null;
        while(node != null){
            if(node.next == null){
                tail = node;
            }
            node = node.next;
            listLen++;
        }
        k = k%listLen;
        if(k == 0)return head;
        //find the listLen - k th node.
        ListNode dumb = new ListNode(0);
        dumb.next = head;
        ListNode p = dumb;
        int count = 0;
        while(count < listLen - k){
            p = p.next;
            count++;
        }
        ListNode second = p.next;
        p.next = null;
        
        dumb.next = second;
        tail.next = head;
        return dumb.next;
        
        
        
    }
}