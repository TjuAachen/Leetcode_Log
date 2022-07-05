import math
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #calculate the integer part first
        sym = - 2
        if numerator < 0:
            numerator = - numerator
            sym += 1
        if denominator < 0:
            sym += 1
            denominator = - denominator
        
        integer_part = numerator // denominator
        
        str_integer_part = str(integer_part) 
        numerator -= integer_part * denominator
        
        
        num2pos = {}
        #calculate the result for exactly divisible
        def calculate(numerator, denominator):
            ten_count = 0
            str_res = ''
            while(numerator < denominator):
                numerator *= 10
                ten_count += 1
            temp_res = numerator // denominator
            str_res = '0'*(ten_count - 1)+str(temp_res)
            new_numerator = numerator - temp_res * denominator
            return new_numerator, str_res
        decimal = []
        while(numerator > 0 and numerator not in num2pos):
            num2pos[numerator] = len(decimal)
            numerator, str_res = calculate(numerator, denominator)
            decimal.append(str_res)
        if numerator > 0:
            decimal.insert(num2pos[numerator],'(')
            decimal.append(')')
        
        if sym == -1 and (integer_part != 0 or decimal):
            str_integer_part = '-' + str_integer_part
        if decimal:
            return str_integer_part +'.'+ ''.join(decimal)
        return str_integer_part
        