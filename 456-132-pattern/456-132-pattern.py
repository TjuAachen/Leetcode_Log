class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        c = -float('inf')
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] < c:
                return True
            if not stack or nums[i] < stack[-1]:
                stack.append(nums[i])
            else:
                while(stack and stack[-1] < nums[i]):
                    c = max(c, stack.pop())
                stack.append(nums[i])
        return False
            
        