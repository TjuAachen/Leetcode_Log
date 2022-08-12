class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while(b != 0):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        if a <= max_int:
            return a
        return ~(a^mask)
        