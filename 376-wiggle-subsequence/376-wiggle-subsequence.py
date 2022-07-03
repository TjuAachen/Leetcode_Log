class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        max_length = 1
        n = len(nums)
        #0:positive, 1:negative
        dp = [[1] * 2 for _ in range(n)]
        for i in range(1, n):
            for j in range(2):
                #positive
                if j == 0:
                    for k in range(i-1,-1,-1):
                        if nums[k] < nums[i]:
                            dp[i][j] = max(dp[i][j],dp[k][1] + 1)
                else:
                    for k in range(i-1,-1,-1):
                        if nums[k] > nums[i]:
                            dp[i][j] = max(dp[i][j],dp[k][0] + 1)                  
            max_length = max(max_length, max(dp[i]))
        return max_length
        