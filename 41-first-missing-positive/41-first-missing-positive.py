class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_pos = 0
        total_min = 2**31
        total_max = 0
        total = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if num > 0:
                num_pos += 1
                total_min = min(total_min, num)
                total_max = max(total_max, num)
                total += num
            else:
                nums[i] = 0           
        if total_min > 1:
            return 1 
#        if num_pos > num_max - num_min + 1:
#            return num_max+1
        left, right = 1, total_max+1
        def validate(left ,mid):
            count = 0
            occur = False
            num_min, num_max = 2**31, 1
            for num in nums:
                if left <= num <= mid:
                    num_min = min(num_min,num)
                    num_max = max(num_max, num)
                    count += 1
            if num_max - num_min + 1 > count:
                return True, True
            for i,num in enumerate(nums):
                if left <= num%(total_max+1) <= mid:
                    nums[nums[i]%(total_max+1)-total_min] += (total_max+1)
            total = 0
            for i,num in enumerate(nums):
                if num >= (total_max+1):
                    total += 1
                    nums[i] = num%(total_max+1)
                if nums[i] == mid:
                    occur = True

            if total == mid - left + 1:
                return False, occur
            else:
                return True, occur
            
            
        while(left < right):
            mid = left + (right - left) // 2
            final = validate(left, mid)
            if final[0]:
                if final[1]:
                    right = mid-1
                else:
                    right = mid
            else:
                if final[1]:
                    left = mid + 1
                else:
                    left = mid
        return left
            
        
                