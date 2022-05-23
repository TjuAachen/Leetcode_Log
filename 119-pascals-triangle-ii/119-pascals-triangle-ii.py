class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [0 for _ in range(rowIndex+1)]
        for row in range(rowIndex+1):
            for i in range(row,-1,-1):
                if i == 0 or i == row:
                    cur[i] = 1
                else:
                    cur[i] += cur[i-1]
        return cur
        