class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        j = 1
        for i in range(n):
            res.append(j)
            if j * 10< n + 1:
                j *= 10
            else:
                while(j%10 == 9 or j > n-1):
                    j //= 10
                j += 1
        return res
            