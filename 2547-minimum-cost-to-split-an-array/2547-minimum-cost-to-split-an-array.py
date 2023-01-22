class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        self.n = len(nums)
        dp = [float('inf')] * (self.n + 1)
        dp[0] = 0
        
        for end in range(1, self.n + 1):
            numCount = defaultdict(int)
            curVal = 0
            for start in range(end - 1, -1, -1):
                curNum = nums[start]
                if curNum in numCount:
                    if numCount[curNum] == 1:
                        curVal += 2
                    else:
                        curVal += 1
                numCount[curNum] += 1
                dp[end] = min(dp[end], dp[start] + curVal + k)
        
        return dp[-1]
        
        
        
    

        
        