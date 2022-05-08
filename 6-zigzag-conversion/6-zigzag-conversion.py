class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        for index, char in enumerate(s):
            if index%(2*(numRows-1)) == 0:
                res[0].append(char)
            else:
                row_number = index%(2*(numRows-1))
                if row_number > numRows - 1:
                    row_number = 2*(numRows-1) - row_number
                res[row_number].append(char)
        total = ''
        for row in res:
            total += ''.join(row)
        return total
            
            
            
        