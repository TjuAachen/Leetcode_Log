class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for i, num in enumerate(nums):
            if first == float('inf'):
                first = num
            else:
                if first < num:
                    if second == float('inf'):
                        second = num
                    else:
                        if second < num:
                            return True
                        else:
                            second = num
                else:
                    first = num
        return False
                    
        