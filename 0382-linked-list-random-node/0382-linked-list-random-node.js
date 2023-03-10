/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    Solution.head = head;
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    var head = Solution.head;
    var cur = head;
    var chosenVal = 0;
    var scope = 1;
    
    while (cur != null) {
        if (Math.random() < 1.0 / scope) {
            chosenVal = cur.val;
        }
        scope += 1;
        cur = cur.next;
    }
    
    return chosenVal;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */