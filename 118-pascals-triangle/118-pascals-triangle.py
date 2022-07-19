class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1] * (i+1) for i in range(numRows)]
        
        for i in range(2, numRows):
            for elem in range(1, len(res[i]) - 1):
                res[i][elem] = res[i-1][elem-1] + res[i-1][elem]
        return res
        