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
    public boolean isPalindrome(ListNode head) {
        //find the mid point
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode reverseHead = reversePalindrome(slow);
        while(reverseHead != null && head != null){
            if (reverseHead.val != head.val){
                return false;
            }
            reverseHead = reverseHead.next;
            head = head.next;
        }
        return true;
        
    }
    public ListNode reversePalindrome(ListNode head){
        ListNode prev = null;
        ListNode cur = head;
        ListNode next = null;
       // ListNode next = head.next;
        while(cur != null){
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
        
        
    }
}