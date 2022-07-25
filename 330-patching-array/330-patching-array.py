from bisect import *
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        #maximum added
        count = 0
        nums_len = len(nums)
        prefix = [0] * (nums_len + 1)
        def power_of_two(temp):
            count = 0
            while(temp != 0):
                temp = temp // 2
                count += 1
            return count-1
        count = power_of_two(n)
        record = {}
        for ind,num in enumerate(nums):
            record[num] = ind
            #prefix[i+1] = prefix[i] + num
        
        
        i = 0
        ans = 0
        upper_limit = 0
        prev_add = 0
        
        while(upper_limit < n):
         #   print(upper_limit, i)
            if i < nums_len:
                cur = nums[i]
            else:
                cur = upper_limit + 1
            while(upper_limit+1 < cur):
                upper_limit += upper_limit + 1
                ans += 1
                if upper_limit >= n:
                    return ans
            if upper_limit+1 >= cur:
                upper_limit += cur
                if i >= nums_len:
                    ans += 1
           # print(upper_limit, ans)
            i += 1
        return ans
                    
                
            
        
        
        
        
        