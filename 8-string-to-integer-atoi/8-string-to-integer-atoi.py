class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        dfa = [{'+-':1,'alpha':3,'whitespace':0,'digit':2,'.':3},
               {'digit':2,'+-':3,'alpha':3,'whitespace':3,'.':3},
               {'digit':2,'+-':3,'alpha':3,'whitespace':3,'.':3},
               {'digit':3,'+-':3,'alpha':3,'whitespace':3,'.':3}
            
        ]
        cur = 0
        sign = 1
        res = 0
        for char in s:
            if char in ['+','-']:
                group = '+-'
                if char == '-' and cur == 0:
                    sign = -1
            elif char == ' ':
                group = 'whitespace'
            elif 'a' <= char.lower() <= 'z':
                group = 'alpha'
            elif char == '.':
                group = '.'
            else:
                group = 'digit'
                res = 10*res + int(char)
            if group not in dfa[cur]:
                break
            cur = dfa[cur][group]
            if cur == 3:
                break
        if -2**31<= res*sign <= 2**31-1:
            return res*sign
        elif res*sign < -2**31:
            return -2**31
        else:
            return 2**31-1
            
                
        