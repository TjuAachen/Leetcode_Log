class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pos = 0
        while(left != right):
            left = left // 2
            right = right // 2
            pos += 1
        return left << pos
            
        