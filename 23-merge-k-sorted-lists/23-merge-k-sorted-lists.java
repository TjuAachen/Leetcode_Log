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
    public ListNode mergeKLists(ListNode[] lists) {
        //divide and conquer
        int size = lists.length;
        if (size == 1){
            return lists[0];
        }else if(size == 0){
            return null;
        }
        int median = size / 2;
        ListNode left_half = this.mergeKLists(Arrays.copyOfRange(lists , 0, median));
        ListNode right_half = this.mergeKLists(Arrays.copyOfRange(lists, median, size));
        //merge two lists
        ListNode left = left_half;
        ListNode right = right_half;
        ListNode merged_list = new ListNode(0);
        ListNode p = merged_list;
        
        while(left != null || right != null){
            int left_val = Integer.MAX_VALUE;
            int right_val = Integer.MAX_VALUE;
            if(left != null){
                left_val = left.val;
            }
            if(right != null){
                right_val = right.val;
            }
            int min_val = Math.min(left_val, right_val);
            if(left_val == min_val){
                ListNode nxt = left.next;
                p.next = left;
                left.next = null;
                left = nxt;
            }else{
                ListNode nxt = right.next;
                p.next = right;
                right.next = null;
                right = nxt;
            }
            p = p.next;

        }
        return merged_list.next;
        
        
        
    }
}