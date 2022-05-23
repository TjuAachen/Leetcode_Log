class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev, cur = [], []
        for row in range(rowIndex+1):
            cur = []
            for i in range(1+row):
                if i == 0 or i == row:
                    cur.append(1)
                else:
                    cur.append(prev[i-1]+prev[i])
            prev = cur[:]
        return cur
        