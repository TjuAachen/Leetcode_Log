class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final(s):
            stack = []
            for i in s:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return ''.join(stack)
        if final(s) == final(t):
            return True
        return False