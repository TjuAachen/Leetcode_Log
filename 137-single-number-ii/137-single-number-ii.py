class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            bit_count = 0
            for num in nums:
                bit = (1 << i) & num
                if bit != 0:
                    bit_count += 1
            if bit_count % 3 != 0:
                ans += (1 << i)
        if ans > 2 ** 31 -1:
            return ans - (1<<32)
        return ans
        