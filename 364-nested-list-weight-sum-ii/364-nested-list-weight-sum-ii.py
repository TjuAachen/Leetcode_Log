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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        global maxDepth, total_sum
        maxDepth = 1
        total_sum = 0
        def sum_integers(nestedInteger, depth):
            global maxDepth, total_sum
            if nestedInteger.isInteger():
                total_sum += nestedInteger.getInteger()
                return nestedInteger.getInteger() * depth
            ans = 0
            for nxt in nestedInteger.getList():
                ans += sum_integers(nxt, depth + 1)
                maxDepth = max(maxDepth, depth + 1)
            return ans
        
        depth_sum = 0
        for nestedInteger in nestedList:
            depth_sum += sum_integers(nestedInteger, 1)
      #  print(total_sum, depth_sum, maxDepth)
        return total_sum * (maxDepth + 1) - depth_sum
        
        
        
        
        