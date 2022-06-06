import math
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        neg = 2
        sign = 1
        if numerator > 0:
            numerator = -numerator
            neg = neg - 1
        if denominator > 0:
            denominator = - denominator
            neg = neg - 1
        if neg == 1:
            sign = -1
        
        num_digit = len(str(abs(denominator)))
        #if divisible
        if numerator % denominator == 0:
            if sign == -1:
                return '-' +  str(numerator // denominator)
            
            return str(numerator // denominator)
        
        
        def dec2str(integer, time):
            if integer == 0:
                return '0'
            if time == 0:
                return str(integer)
            ans = list(str(integer))
            num_digit = len(ans)
            if time >= num_digit:
                ans = ['0'] * (time - num_digit + 1) + ans  
            return ''.join(ans[-time:])
                   
        
        
        #if not divisible, decide the number if repeating digits
        def division(numer, denom, prev_time):
            # increase by 10 till numer is larger than denom
            time = 0
            while(numer > denom):
                time += 1
                numer = numer * 10
            remainder = numer % denom
            if remainder == 0:
                res = str(numer//denom)
            else:
                res = dec2str(numer // denom, time)
            return res, remainder, time
        
        #keep division until the remainder is equal to the prev numerator
        prev_numerator = 0
        final = str(numerator // denominator) +'.'
        numerator = numerator % denominator
        total_time = 0
        rec_remainder = dict()
        while(numerator not in rec_remainder and numerator != 0):
            rec_remainder[numerator] = total_time
            cur_res, remainder, cur_time = division(numerator, denominator, total_time)
            final += cur_res
            total_time += cur_time
            prev_numerator = numerator
            numerator = remainder
        
        #postprocessing without repeating
        if numerator == 0:
            if sign == -1:
                return '-' + final
            return final
        
        #postprocessing, deal with repeating numbers
        final = list(final)
        final.insert(-(total_time - rec_remainder[numerator]), '(')
        final.append(')')
        if sign == -1:
            return '-' + ''.join(final)
        return ''.join(final)
        
    
            
        