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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p1 = l1;
        ListNode p2 = l2;
        int carry = 0;
        ListNode dumb = new ListNode(-1);
        ListNode p3 = dumb;
        while(l1 != null || l2 != null){
            int l1_val = 0;
            int l2_val = 0;
            if (l1 != null){
                l1_val = l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                l2_val = l2.val;
                l2 = l2.next;
            }
            int add_res = l1_val + l2_val + carry;
            carry = add_res / 10;
            add_res = add_res%10;
            ListNode temp = new ListNode(add_res);
            p3.next = temp;
            p3 = p3.next;
        }
        if (carry > 0){
            ListNode temp = new ListNode(carry);
            p3.next = temp;
        }
        return dumb.next;
    }
}