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
    public ListNode swapPairs(ListNode head) {
        ListNode odd = new ListNode();
        ListNode even = new ListNode();
        ListNode dumb = new ListNode();
        ListNode oddPointer = odd;
        ListNode evenPointer = even;
        ListNode dumbPointer = dumb;
        ListNode p = head;
        int count = 0;
        
        while(p != null){
            ListNode curNode = p;
            ListNode nxt = p.next;
            if(count % 2 == 0){
                evenPointer.next = curNode;
                
                curNode.next = null;
                evenPointer = curNode;
                
            }else{
                oddPointer.next = curNode;
                curNode.next = null;
                oddPointer = curNode;                
            }
            p = nxt;
            count++;
            
        }
        oddPointer = odd.next;
        evenPointer = even.next;
        int index = 0;
        while(oddPointer != null && evenPointer != null){
            
            if(index%2 == 0){
                ListNode nxt = oddPointer.next;
                dumbPointer.next = oddPointer;
                oddPointer.next = null;
                oddPointer = nxt;
            }else{
                ListNode nxt = evenPointer.next;
                dumbPointer.next = evenPointer;
                
                evenPointer.next = null;
                evenPointer = nxt;                
            }
            index++;
            dumbPointer = dumbPointer.next;
        }
        
        if(evenPointer != null){
            dumbPointer.next = evenPointer;
        }
        return dumb.next;
        
        
        
        
        
        
        
        
        
    }
}