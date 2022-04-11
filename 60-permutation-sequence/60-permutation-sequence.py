import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        i = 1
        available = [j+1 for j in range(n)]
        while(len(res) < n):
            factor = math.factorial(n-i)
            num = available[(k-1) //factor]
            available.remove(num)
            k =  k%factor
            res.append(num)
            i = i + 1
        return ''.join([str(i) for i in res])
        