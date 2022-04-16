class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        final = []
        def find(i):
            if len(res) == k:
                final.append(res[:])
                return
            for elem in range(i,n+1):
                res.append(elem)
                find(elem+1)
                res.pop()
        find(1)
        return final
        