# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = self.clean(nestedList)
        self.nextIter = None
        
        
    def clean(self,nestedList):
        i = 0
        while(i < len(nestedList)):
            NestedInteger = nestedList[i]
            if not NestedInteger.isInteger():
                if self.emptyOne(NestedInteger.getList()):
                    nestedList = nestedList[:i] + nestedList[i+1:]
                else:
                    cleaned = self.clean(NestedInteger.getList())
                    if cleaned != None:
                        nestedList = nestedList[:i]+cleaned+nestedList[i+1:]
                        i = i+1
                    else:
                        nestedList = nestedList[:i] + nestedList[i+1:]
            else:
                i = i + 1
        return nestedList
    def next(self) -> int:
        if ((not self.nextIter or not self.nextIter.hasNext())) and (self.nestedList and self.nestedList[0].isInteger()):
            k = self.nestedList.pop(0).getInteger()
            return k
        elif (self.nestedList):
            if (not self.nextIter or not self.nextIter.hasNext()):
                m = self.nestedList.pop(0).getList()
                if m:
                    self.nextIter = NestedIterator(m)
        if self.nextIter:
            return self.nextIter.next()
    def emptyOne(self,nestedList):
        if not nestedList:
            return True        
        elif len(nestedList) == 1:
            n = len(nestedList)
            nxt = nestedList[0].getList()
            if nxt:
                return self.emptyOne(nxt)
            else:
                return not nestedList[0].isInteger()
        else:
            return False
        
    def hasNext(self) -> bool:
        if (not self.nestedList) and (not self.nextIter or not self.nextIter.hasNext()):
            return False
        else:
            return True
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())