class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for char in path.split('/'):
            if char =='..':
                if stack:
                    stack.pop()
            elif char == '.' or not char:
                continue
            else:
                stack.append(char)
        return ('/'+'/'.join(stack))
            
        