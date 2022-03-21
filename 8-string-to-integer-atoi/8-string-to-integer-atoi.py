class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        res = 0
        power = 1
        flag = False
        bound = 2147483648
        for index,char in enumerate(s):
            if index == 0:
                if char == '-':
                    sign = -1
                    flag = True
                elif char == '.':
                    return 0
                elif char == '+':
                    sign = 1
                    flag = True
                elif (char > '9' or char <'0'):
                    return 0                    
            if flag and char == '.':
                return sign*res
            elif (char > '9' or char <'0') and flag and index>0:
                return sign*res
            if '0' <= char <= '9':
                flag = True
                if sign == 1 and bound-1-res*10>=int(char):
                    res = res*10 + int(char)
                elif sign == 1:
                    return bound - 1
                if sign == -1 and bound-res*10>=int(char):
                    res = res*10 + int(char)
                elif sign == -1:
                    return -1*bound
        return sign*res
                
            