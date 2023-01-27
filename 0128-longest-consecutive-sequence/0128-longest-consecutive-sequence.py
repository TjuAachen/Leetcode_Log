class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #当前数所在的最长子序列长度
        dp = defaultdict(int)
        maxLength = 0
        
        for num in nums:
            if num in dp:
                continue
            left, right = 0, 0
            if num - 1 in dp:
                left = dp[num - 1]
            leftMost = num - left                
            if num + 1 in dp:
                right = dp[num + 1]
            rightMost = num + right            
            curMax = 1 + left + right
            dp[leftMost] = curMax
            dp[rightMost] = curMax
            dp[num] = curMax
            maxLength = max(curMax, maxLength)
        
        return maxLength
            
            
            