class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """
        nrow1, ncol1 = len(mat1), len(mat1[0])
        nrow2, ncol2 = len(mat2), len(mat2[0])
        
        res = [[0] * ncol2 for _ in range(nrow1)]
        for i in range(nrow1):
            for j in range(ncol1):
                if mat1[i][j] != 0:
                    for m in range(ncol2):
                        if mat2[j][m] != 0:
                            res[i][m] += mat2[j][m] * mat1[i][j]
        return res
        