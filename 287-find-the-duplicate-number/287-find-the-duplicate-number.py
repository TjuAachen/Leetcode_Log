class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_min, num_max = len(nums) + 1, 0
        for num in nums:
            num_min = min(num, num_min)
            num_max = max(num, num_max)
        left, right = num_min, num_max
        def helper(left, mid):
            total = 0
            for num in nums:
                if  left <= num <= mid:
                    total += 1
            if mid - left + 1 < total:
                return True
            else:
                return False
        while(left < right):
            mid = left + (right - left) // 2
            if helper(left, mid):
                right = mid 
            else:
                left = mid + 1
        return left
        