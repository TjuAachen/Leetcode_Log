class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [{'+-':1,'.':2,'digit':3},
               {'.':2,'digit':3},
               {'digit':7},
               {'digit':3,'e':4,'.':7},
               {'digit':5,'+-':6},
               {'digit':5},
               {'digit':5},
               {'digit':7,'e':4}]
        cur = 0
        for char in s:
            if char in ['+','-']:
                group = '+-'
            elif '0' <= char <= '9':
                group = 'digit'
            elif char == '.':
                group = '.'
            elif char in ['e','E']:
                group = 'e'
            else:
                return False
            if group not in dfa[cur]:
                return False
            cur = dfa[cur][group]
        return cur in [3,5,7]
        
        