class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        s = list(str(sign*x))
        value = 0
        for index in range(len(s)-1,-1,-1):
            if sign == -1 and  2147483648 - value*10  >= int(s[index]):
                value = value*10 + int(s[index])
            elif sign == 1 and   2147483647-value*10 >= int(s[index]):
                value = value*10 + int(s[index])
            else:
                return 0
        return value*sign
            
            
                
        
        