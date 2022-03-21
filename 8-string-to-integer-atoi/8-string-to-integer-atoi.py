class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        res = 0
        power = 1
        i = 0
        bound = 2147483648
        if s=="":
            return 0
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            sign = 1
            i = 1
        for char in s[i:]:
            if char.isdigit():
                res = 10*res + ord(char) - ord('0')
            else:
                break
        if sign == -1:
            return max(-res,-1*bound)
        else:
            return min(res,bound-1)
        return sign*res
                
            