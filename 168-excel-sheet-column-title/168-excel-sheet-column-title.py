class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        
        
        #decrease columnNumber by 26 till less than 0
        while(columnNumber > 0):
            cur = (columnNumber -1) % 26
            columnNumber = (columnNumber - cur) // 26
            cur_char = chr(ord('A') + cur)
            ans = cur_char + ans
        return ans