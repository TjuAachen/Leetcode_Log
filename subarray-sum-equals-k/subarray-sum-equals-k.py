class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumSum = 0
        dic = {0:1}
        res = 0
        for i, elem in enumerate(nums):
            cumSum += elem            
            desire = cumSum - k
            res += dic.get(desire,0)
            if cumSum not in dic:
                dic[cumSum] = 1
            else:
                dic[cumSum] += 1
        return res
            
            
            