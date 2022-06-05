class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        stack = []
        flag_upper = False
        flag_lower = False
        for num in nums:
            if num < lower or num > upper:
                continue
            stack.append(num)
            if num == upper:
                flag_upper = True
            if num == lower:
                flag_lower = True
        if not flag_upper:
            stack.append(upper+1)
        if not flag_lower:
            stack = [lower-1] + stack
        length = len(stack)
        res = []
        def generate(l, r):
            if r - l < 2:
                return 
            if l + 2 == r:
                return str(l+1)
            return str(l+1) + '->' + str(r-1)
        for ind, elem in enumerate(stack):
            if ind < length - 1:
                missing_range = generate(elem, stack[ind + 1])
                if missing_range:
                    res.append(missing_range)
        return res
                
        