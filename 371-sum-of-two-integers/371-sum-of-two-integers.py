class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        
        if x < y:
            x, y = y, x

        sign = 1
        if a * b > 0:
            if a < 0:
                sign = -1
            while y:
                temp_x, temp_y = (x^y), (x&y) << 1
                x, y = temp_x, temp_y
        else:
            if abs(max(a,b)) < abs(min(a,b)):
                sign = -1
              #  print(sign)
            while y:
                temp_x, temp_y = (x^y), ((~x)&y)<<1
                x, y = temp_x, temp_y
      #  print(abs(max(a,b)), abs(min(a,b)))
        return x*sign 
        