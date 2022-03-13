class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        record = dict()
        record[')'] = '('
        record[']'] = '['
        record['}'] = '{'
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if (len(stack)==0) or stack[-1] != record[i]:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
                
            
        