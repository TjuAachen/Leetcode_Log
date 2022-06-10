class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        pos = 0
        while(pos < 32):
            cur = (1 << pos) & n
            if cur != 0:
                res += (1 << (31 - pos))
            pos += 1
        return res
        