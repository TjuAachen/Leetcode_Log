class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #monotonic stack
        stack = []
        n = len(nums)
        res = 0
        for i, curVal in enumerate(nums + [float('-inf')]):
  
            while(stack and nums[stack[-1]] > curVal):
                popped = stack.pop()
                if stack:
                    bottom = stack[-1]
                else:
                    bottom = -1
                res -= nums[popped] * (i - popped) * (popped - bottom)
            stack.append(i)
        stack = []
        for i, curVal in enumerate(nums + [float('inf')]):

            while(stack and nums[stack[-1]] < curVal):
                popped = stack.pop()
                if stack:
                    bottom = stack[-1]
                else:
                    bottom = -1
                res += nums[popped] * (i - popped) * (popped - bottom)
            stack.append(i)
        return res       
                
                
        