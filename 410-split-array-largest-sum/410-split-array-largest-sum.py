class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        max_num = max(nums)
        left, right = max_num, sum(nums)
        def validate(sub):
            total = 0
            res = 0
            for index, num in enumerate(nums):
                total += num
                if total > sub:
                    res += 1
                    total = num
            res += 1
            return res
                    
        while(left < right):
            mid = left + (right - left)//2
            result = validate(mid)
            if result == m and (mid == max_num or validate(mid - 1) != m):
                return mid
            elif result == m:
                right = mid - 1
            elif result > m:
                left = mid + 1
                
            elif result < m:
                right = mid - 1
        return left
        
            
        