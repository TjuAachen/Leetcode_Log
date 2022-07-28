from bisect import *
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = []
        for num in nums:
            if not a or a[-1] < num:
                a.append(num)
            elif a[0] < num:
                a[-1] = num
            else:
                a[0] = num
            if len(a) > 2:
                return True
        return False
        