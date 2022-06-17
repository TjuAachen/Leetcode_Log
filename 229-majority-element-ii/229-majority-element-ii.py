class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #voting algorithm
        length = len(nums)
        candidate1, candidate2, count1, count2 = None, None, 0,0
        #three distinct elements are eliminated together
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 = count1 - 1
                count2 = count2 - 1
        res = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > length // 3:
                res.append(candidate)
        return res
            
        