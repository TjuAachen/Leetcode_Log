class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        size = len(nums)
        dp = [[0]*3**numSlots for _ in range(size+1)]
        for i in range(1, size + 1):
            for state in range(3**numSlots):
                for j in range(numSlots):
                    if (state//(3**j))%3 > 0:
                        dp[i][state] = max(dp[i][state],dp[i-1][state-3**j]+((j+1)&nums[i-1]))
        return max(dp[size])
        