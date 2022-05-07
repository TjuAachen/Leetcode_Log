class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono_stack = []
        k = - float('inf')
        if len(nums) < 3:
            return False
        for index in range(len(nums)-1,-1,-1):
            i = nums[index]
            if i < k:
                return True
            while mono_stack and mono_stack[-1] < i:
                k = max(k,mono_stack.pop())
            mono_stack.append(i)
        return False