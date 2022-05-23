class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]
        for row in range(numRows):
            for i in range(1+row):
                if i == 0 or i == row:
                    res[row].append(1)
                else:
                    res[row].append(res[row-1][i-1] + res[row-1][i])
        return res
                    
                
        