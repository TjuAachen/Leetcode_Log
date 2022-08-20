class Solution:
    def integerReplacement(self, n: int) -> int:
        #reversed thinking
        count = 0
        while(n != 1):
            if n%2 == 0:
                n = n//2
            else:
                if ((n>>1)&1)==0 or n == 3:
                    n = n - 1
                else:
                    n = n +1
            count += 1
          #  print(n)
           # print(n, count_plus, count_minus)
        return count
            
                
        