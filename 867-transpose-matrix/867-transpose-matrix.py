class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(matrix), len(matrix[0])
        transposed = [[0]*nrow for _ in range(ncol)]
        for i in range(nrow):
            for j in range(ncol):
                transposed[j][i] = matrix[i][j]
        return transposed
                
        