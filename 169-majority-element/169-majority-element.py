class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bit_pos = [0] * 32
        def count_bit(num):
            for pos in range(32):
                bit = (1<<pos) & num
                if bit != 0:
                    bit_pos[pos] += 1
            
        for num in nums:
            count_bit(num)
        
        ans = 0
        for ind, bit_count in enumerate(bit_pos):
            if bit_count > n // 2:
                ans += (1 <<ind)
        return ans
                
        