class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        flag_upper = False
        flag_lower = False
        
        if not nums or nums[-1] != upper:
            nums.append(upper+1)
        if not nums or nums[0] != lower:
            nums = [lower-1] + nums
        length = len(nums)
        res = []
        def generate(l, r):
            if r - l < 2:
                return 
            if l + 2 == r:
                return str(l+1)
            return str(l+1) + '->' + str(r-1)
        for ind, elem in enumerate(nums):
            if ind < length - 1:
                missing_range = generate(elem, nums[ind + 1])
                if missing_range:
                    res.append(missing_range)
        return res
                
        