class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, start, target):
            left, right = start, len(nums) - 1
            res = []
            while(left < right):
                l, r = nums[left], nums[right]
                sum_ij = l + r
                if sum_ij < target:
                    left = left + 1
                elif sum_ij == target:
                    res.append([nums[left], nums[right]])
                    while(left < right and nums[left] == l): 
                        left += 1
                    while(left < right and nums[right] == r): 
                        right -= 1
                else:
                    right = right - 1

            return res
        nums.sort()
        final = []
        i = 0
        while(i < len(nums)):
            target = -nums[i]
            res = twoSum(nums, i + 1, target)
            if res:
                final = final + [[nums[i]]+j for j in res]
            while(i < len(nums)-1 and nums[i+1] == -target):
                i = i + 1
            i = i + 1
        return final
                
                
                    