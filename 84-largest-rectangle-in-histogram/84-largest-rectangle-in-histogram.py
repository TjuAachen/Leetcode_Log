class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        record = [-1]*n
        for i in range(n-1,-1,-1):
            while(stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                record[i] = stack[-1]
            stack.append(i)
        stack = []
        record_l = [-1]*n
        for i in range(n):
            while(stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                record_l[i] = stack[-1]
            stack.append(i) 
        dp = heights[:]
        for i in range(n):
            if record[i] != -1:
                right = record[i] - 1
            elif record[i] == -1:
                right = n - 1
            if record_l[i] != -1:
                left = record_l[i] + 1
            elif record_l[i] == -1:
                left = 0
            dp[i] = (right-left+1)*heights[i]
      #  print(record,record_l)
        return max(dp)
                
        