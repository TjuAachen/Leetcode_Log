class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        record = set()
        dp =[0] * len(nums)
        prev_max_step = None
        max_step = 0
        for ind, num in enumerate(nums):
            prev_max_step = 0
            while stack and stack[-1][1] <= num:
                popped = stack.pop()
                prev_max_step = max(prev_max_step, popped[-1])
            if stack:
                dp[ind] = prev_max_step + 1
            stack.append([ind, num, dp[ind]])
            max_step = max(max_step, dp[ind])
       #     print(stack, num, dp[ind], prev_max_step)
        return max_step
        
        
        