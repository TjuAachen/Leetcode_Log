class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        
        if n - k == 0:
            return '0'
        for char in num:
            while(stack and k and stack[-1] > char):
                stack.pop()
                k -= 1
            stack.append(char)
        if k != 0:
            stack = stack[:-k]
        res = ''.join(stack).lstrip('0')
        if len(res) > 0:
            return res
        return '0'
          