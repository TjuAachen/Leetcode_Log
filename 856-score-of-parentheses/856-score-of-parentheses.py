class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        for char in s:
            if char == "(":
                stack.append(res)
                res = 0
            else:
                res = stack[-1]+max(res<<1,1)
                stack.pop()
        return res
        