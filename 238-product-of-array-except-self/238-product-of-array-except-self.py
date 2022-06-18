from bisect import bisect
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        res = 1
        for ind, num in enumerate(nums):
            answer[ind] = res
            res = res * num
        
        res = 1
        nums = nums[::-1]
        n = len(nums)
        for ind, num in enumerate(nums):
            answer[n -1- ind] = answer[n -1- ind] * res
            res = res * num
        return answer
            
            
        