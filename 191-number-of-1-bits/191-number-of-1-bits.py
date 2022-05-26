class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            num = n&(1<<i)
            if num != 0:
                count += 1
        return count