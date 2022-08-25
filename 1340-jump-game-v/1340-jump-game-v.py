from heapq import *
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        inc_stack = []
        dec_stack = []
        n = len(arr)
        left_largest = [-float('inf')] * n
        right_largest = [float('inf')] * n
        heap = []
        for i, num in enumerate(arr):
            while(dec_stack and arr[dec_stack[-1]] <= num):
                popped_idx = dec_stack.pop()
                right_largest[popped_idx] = i
            dec_stack.append(i)  
            while(inc_stack and arr[inc_stack[-1]] < num):
                inc_stack.pop()
            if inc_stack:
                left_largest[i] = inc_stack[-1]
            inc_stack.append(i)
            heappush(heap,[num, i])
        
        dp = [1] * n
        ans = 0
        while(heap):
            num, i = heappop(heap)
            left = max([left_largest[i] + 1, i - d,0])
            right = min([right_largest[i] - 1, i + d,n-1])
            
           # print(i, left)
            for j in range(left, i):
                dp[i] = max(dp[i], dp[j] + 1)
            for j in range(i+1, right+1):
                dp[i] = max(dp[i], dp[j] + 1)           
            ans = max(ans, dp[i])
       # print(left_largest, right_largest)
       # print(dp)
        return ans
            
        