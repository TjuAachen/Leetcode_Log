# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        i = 0
        s_len = len(s)
        stack_left = []
        res = None
        while(i < s_len):
            cur = s[i]
            if cur == '[':
                res = NestedInteger()
                stack_left.append(res)
                i = i + 1
            elif cur == ']':
                res = stack_left.pop()
                if stack_left:
                    stack_left[-1].add(res)
                i = i + 1
            elif cur == ',':
                i = i + 1
            else:
                sign = 1
                num = 0
                if cur == '-':
                    sign = -1
                    i = i + 1
               # cur = s[i]
                while(i < s_len and s[i] != ',' and s[i] != '[' and s[i] != ']'):
                    cur = s[i]
                 #   print(cur)
                    num = 10*num + int(cur)
                    i = i + 1
                new_element = NestedInteger(sign*num)
               # print(num)
                if stack_left:
                    stack_left[-1].add(new_element)
                #    print(stack_left, new_element)
                else:
                    res = new_element
        return res
        
                
                
                
        