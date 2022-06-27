class Solution:
    def minPartitions(self, n: str) -> int:
        cur = 0
        for num in n:
            cur = max(cur, int(num))
        return cur
        