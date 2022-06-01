class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        cumsum=0
        for i in range(len(nums)):
            cumsum+=nums[i]
            result.append(cumsum)
        return result
            