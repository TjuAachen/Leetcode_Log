# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        #divide and conquer by setting the median as the root in each subcase.
        def find_med(head):
            fast, slow = head.next.next,head 
            while(fast and fast.next):
                fast = fast.next.next
                slow = slow.next
            return slow
        def generate(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            slow = find_med(head)
            left_list, right_list = head, slow.next.next
            root = TreeNode(slow.next.val)
            slow.next = None
            left, right= generate(left_list), generate(right_list)
            root.left, root.right = left, right
            return root
        return generate(head)