class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def clip(final):
            if -2**31 <= final <= 2**31-1:
                return final
            else:
                if sign == -1:
                    return -2**31
                else:
                    return 2**31-1
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            final = sign*dividend
            return clip(final)
        res = dividend
        count = 0
        factor = divisor
        while(res > 0):
            res = res - factor
            factor = factor + divisor
            count += 1        
        if res == 0:
            final = sign*(count + 1)*count//2
            return clip(final)
        res = res + factor - divisor
        prev_total = (count - 1)*count//2
        for i in range(1, count+1):
            res = res - divisor
            if res < 0:
                final = sign*(prev_total + i - 1)
                return clip(final)
            elif res == 0:
                final = sign*(prev_total + i)
                return clip(final)
        