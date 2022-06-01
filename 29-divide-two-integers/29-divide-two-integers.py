class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31 
        sym = 2
        sign = 1
        if (dividend == MIN_INT and divisor == -1):
            return MAX_INT
        if (dividend > 0):
            sym = sym - 1
            dividend = - dividend
        if (divisor > 0):
            sym = sym - 1
            divisor = - divisor
        
        if (sym == 1):
            sign = -1
        def divide_core(dividend, divisor):
            ans = 0
            while(dividend <= divisor):
                value = divisor
                temp = 1
                while(value >= - 2 ** 30 and value + value >= dividend):
                    value = value << 1
                    temp = temp << 1
                ans += temp
                dividend = dividend - value
            return ans
        res = divide_core(dividend, divisor)
        return sign * res
        
        