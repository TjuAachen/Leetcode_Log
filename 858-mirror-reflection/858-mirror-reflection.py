class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        n = 1
        while(n * q%p != 0):
            n += 1

        if n%2 == 0:
            return 2
        #print(n*q, p)
        divisor = n*q//p
        if divisor % 2 == 0:
            return 0
        return 1
        
        
        
        
        