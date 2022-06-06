class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        #edge case numer = 0
        if numerator == 0:
            return '0'
        #if divisible:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        #set sign and convert to neg
        neg = 2
        sign = 1
        if numerator > 0:
            numerator = - numerator
            neg = neg - 1
        if denominator > 0:
            denominator = - denominator
            neg = neg - 1
        if neg == 1:
            sign = -1
        
        #long division
        final = ''
        rec_remainder = {}
        if sign == -1:
            final += '-' + str(numerator // denominator) + '.'
        else:
            final += str(numerator // denominator) + '.'
        remainder = numerator % denominator
        numerator = remainder
        rec_remainder[remainder] = 0
        digit_pos = 0
        while(remainder != 0):
            numerator = remainder * 10
            remainder = numerator % denominator
            digit_pos += 1
            final += str(numerator // denominator)
            if remainder not in rec_remainder:
                rec_remainder[remainder] = digit_pos
            else:
                break
            

        if remainder == 0:
            return ''.join(final)
        #post processing
        final = list(final)
        final.insert(-digit_pos +rec_remainder[remainder],'(')
        final.append(')')
        return ''.join(final)
        
            
            
        
        