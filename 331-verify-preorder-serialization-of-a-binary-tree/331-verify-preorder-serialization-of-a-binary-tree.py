class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = []
       
        def str2node(char):
           # print(char)
            if char == '#':
                return None
            return int(char)
        for char in preorder:
            val = str2node(char)
            if not stack or stack[-1] != None:
                stack.append(val)
            else:
                while(stack and stack[-1] == None):
                    stack.pop()
                if stack:
                    popped = stack.pop()
                    if popped == None:
                        return False
                    stack.append(val)
                else:
                    return False
       # print(stack)
        while(stack and not stack[-1]):
            stack.pop()        
        if stack:
            return False
        return True
        
            
        