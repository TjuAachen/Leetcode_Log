class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeatedNum = 0
        totalSum = 0
        nums.sort()
        for i, num in enumerate(nums):
            if i < len(nums) - 1 and num == nums[i + 1]:
                repeatedNum = num
            totalSum += num
        n = len(nums)
        expectedSum = (n + 1) * n // 2
        diff = - totalSum + expectedSum
        missedNum = diff + repeatedNum
        return [repeatedNum, missedNum]