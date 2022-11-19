from sortedcontainers import *
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        trees.sort()
        
        leftMostPoint = trees[0]
        
        res = set()
        res.add(tuple(leftMostPoint))
        
        start = leftMostPoint
        
        while(True):
            
            temp = self.findCloest(start, trees)
            newTemp = []
            
            for point in temp:
                if tuple(point) in res:
                    continue
                newTemp.append(point)
            
  
            if not newTemp:
                return list(res)

            dist = -float('inf')
            
            for point in newTemp:
                res.add(tuple(point))
                curDist = (point[0] - start[0])**2 + (point[1] - start[1])**2

                if curDist >= dist:
                    nxtStart = point
                    dist = curDist
            start = nxtStart
                    
        
                    
            
        
    
    def findCloest(self,start, trees):
        
        prev = None
        temp = []
        
        for x, y in trees:
            key = tuple([x, y])
            if x == start[0] and  y == start[1]:
                continue
            cur = [x - start[0], y - start[1]]
            if not prev:
                temp.append([x, y])
                prev = cur
            elif prev:
                val = self.crossProduct(prev, cur)
                if val < 0:
                    temp = []
                    temp.append([x, y])
                    prev = cur
                if val == 0:
                    temp.append([x, y])
          ###  temp.append([x, y])
          #  print(prev, temp, cur, start)
            
            
        
        return temp
    
        
    def crossProduct(self, p1, p2):
         
        return p1[0] * p2[1] - p1[1] * p2[0]
        
        
            