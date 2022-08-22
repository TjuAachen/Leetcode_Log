class Solution:
    def isPowerOfFour(self, n: int) -> bool:
      #  print(n&(n-1))
        if n&(n-1):
            return False
        if n&(0x55555555):
            return True
        return False
       # if n&(0x)
            
        