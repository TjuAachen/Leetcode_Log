class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res = res^num
        diff = res&(-res)
        new_bit = 0
        for num in nums:
            if num&diff:
                new_bit = new_bit^num
        return [new_bit^res, new_bit]