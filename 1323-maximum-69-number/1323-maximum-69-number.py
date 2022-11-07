class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num_str = list(str(num))
        hasRevised = False
        
        for i, curNum in enumerate(num_str):
            if curNum == '6' and not hasRevised:
                hasRevised = True
                num_str[i] = '9'
        
        return int(''.join(num_str))