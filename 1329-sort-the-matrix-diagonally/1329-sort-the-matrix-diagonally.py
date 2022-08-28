from sortedcontainers import SortedList
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #bucket sorting
        #extract diagonal first
        nrow, ncol = len(mat), len(mat[0])
        
        for col in range(ncol):
            diff = 0 - col
            sort_contain = SortedList()
            for row in range(min(diff + ncol, nrow)):
                sort_contain.add(mat[row][row - diff])
            for row in range(min(diff+ncol, nrow)):
                mat[row][row-diff] = sort_contain.pop(0)

        for row in range(1, nrow):
            diff = row
            sort_contain = SortedList()
            for col in range(min(nrow-diff, ncol)):
                sort_contain.add(mat[diff + col][col])
            for col in range(min(nrow-diff, ncol)):
                mat[diff + col][col] = sort_contain.pop(0)

        return mat