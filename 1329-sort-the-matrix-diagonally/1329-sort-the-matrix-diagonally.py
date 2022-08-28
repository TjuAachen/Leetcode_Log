from sortedcontainers import SortedList
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #bucket sorting
        #extract diagonal first
        nrow, ncol = len(mat), len(mat[0])
        diagonals = defaultdict(SortedList)
        
        for row in range(nrow):
            for col in range(ncol):
                diagonals[row-col].add(mat[row][col])
        
        for row in range(nrow):
            for col in range(ncol):
                mat[row][col] = diagonals[row-col].pop(0)
        return mat