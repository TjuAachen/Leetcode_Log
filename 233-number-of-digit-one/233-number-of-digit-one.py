class Solution:
    def countDigitOne(self, n: int) -> int:
        num_digits = len(str(n))
        
        #dp[i] means  the number of 1 in (0,10**i - 1]
        dp = [0] * (num_digits)
        
        
        for i in range(1, num_digits):
            dp[i] = 10*dp[i-1] + 10**(i-1)
        
        def divide_num(num):
            str_num = str(num)
            head = int(str(num)[0])
            if str_num[1:]:
                remaining = int(str(num)[1:])
            else:
                remaining = 0
            return head, remaining
        res = 0
        def num_digit(num):
            head, remaining = divide_num(num)
            num_digits = len(str(num))
            res = 0
            if head == 0 and remaining == 0:
                return 0
            if head == 1:
                res += remaining + 1 + num_digit(remaining) + dp[num_digits - 1]
                
            else:
                #the first position
                res += num_digit(remaining)
                
                #the next position
                res += head * dp[num_digits - 1] + 10**(num_digits - 1)
            return res
        return num_digit(n)
        
        
        
        
                
                
            