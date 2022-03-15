class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        result =[]
        removed = []
        for index, char in enumerate(s):
            if char == '(':
                result.append(index)
            elif char == ')':
                if not result:
                    s[index] = ''
                else:
                    result.pop()
        for m in result:
            s[m] = ''
        return ''.join(s)
        
        