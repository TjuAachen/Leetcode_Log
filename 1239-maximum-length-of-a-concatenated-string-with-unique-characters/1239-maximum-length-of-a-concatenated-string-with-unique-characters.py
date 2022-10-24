class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.combination(arr, 0, [0] * 26, 0)
    
    def combination(self, arr, start,temp, curLength):
        if start == len(arr):
            return curLength
        curString = arr[start]
        curSet = set(curString)
        res = 0
        ifSelected = True
        #selected
        if len(curString) == len(curSet):
            for char in curSet:
                idx = ord(char) - ord('a')
                if temp[idx] > 0:
                    ifSelected = False
                    break
        else:
            ifSelected = False
        if ifSelected:
            for char in curSet:
                idx = ord(char) - ord('a')
                temp[idx] += 1          
            res = max(res, self.combination(arr, start + 1, temp, curLength + len(curString)))
            for char in curSet:
                idx = ord(char) - ord('a')
                temp[idx] -= 1          
        #not selected
        res = max(res, self.combination(arr, start + 1, temp, curLength))
        return res