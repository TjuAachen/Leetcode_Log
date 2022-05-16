class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        #consider the overflow case
        if dividend == MIN_INT and divisor == - 1:
            return MAX_INT
        
        #the sign of result: 1- negative; others-positive
        
        negative = 2
        
        #as -2**31 can be overflow if it is converted to the absolute value, we convert all integers into negative here.
        if dividend > 0:
            dividend = - dividend
            negative = negative - 1
        
        if divisor > 0:
            divisor = -divisor
            negative = negative - 1
        
        #function to find the result
        def divide_core(dividend, divisor):
            ans = 0
            while(dividend <= divisor):
                exponent = 0
                value = divisor
                while(value >= -2**30 and value + value > dividend):
                    
                    value += value
                    exponent += 1
                dividend = dividend - value
                ans += 1<<exponent
            return ans
        
        
        result = divide_core(dividend, divisor)
        
        
        if negative == 1:
            return -result
        else:
            return result
                
        
        