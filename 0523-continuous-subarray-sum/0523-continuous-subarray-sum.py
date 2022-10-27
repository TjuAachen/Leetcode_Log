class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            nums[i] = num%k
        n = len(nums)
        prefix = [0] * (n + 1)
        prefixDict = defaultdict(int)
        prev = 0
        for i in range(n):
            prefix[i + 1] = (prefix[i] + nums[i])%k
            if (prefix[i+1] - k)%k in prefixDict:
                return True
            prefixDict[prev] += 1
            prev = prefix[i + 1]
        return False
        
        