class union_set:
    def __init__(self, n):
        
        self.parent = [i for i in range(n)]
        self.size = [1] * n
      #  self.minVal = [float('inf')] * n
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, p, q):
        parentP, parentQ = self.find(p), self.find(q)
        
        if parentP == parentQ:
            return
        
        if self.size[parentP] <= self.size[parentQ]:
            self.parent[parentP] = parentQ
            self.size[parentQ] += self.size[parentP]
        #    self.minVal[parentQ] = min(self.minVal[parentQ], self.minVal[parentP])
        else:
            self.parent[parentQ] = parentP
            self.size[parentP] += self.size[parentQ]
          #  self.minVal[parentP] = min(self.minVal[parentQ], self.minVal[parentP])

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        #build graph
        graph = defaultdict(list)
        maxGroup = 1
        
        unionSet = union_set(n)
        
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            unionSet.union(p - 1, q - 1)
        
       # totalConnectedNum = 0
        groupMax = defaultdict(int)
        

        
        res = 0
       # print(graph)
        
        for i in range(1, n + 1):
            groupMax[unionSet.find(i - 1)] = -1
        
        for start in range(1, n + 1):
            curRes, curGroup = self.bfsNum(start, graph)
            curParent = unionSet.find(start - 1)
            if curRes == -1:
                continue
            groupMax[curParent] = max(groupMax[curParent], curRes)
            

        for node, val in groupMax.items():
            if val == -1:
                return -1
            res += val
        
        return res
    
    def bfsNum(self, start, graph):
        
        queue = deque()
        group = defaultdict(int)
        
        queue.append([start, 1])
        group[start] = 1
        
        res = 1
        
        while(queue):
           # print(queue)
            popped, curGroupIdx = queue.popleft()
            res = max(res, curGroupIdx)

            for nxt in graph[popped]:
                
                if nxt in group and abs(group[nxt] - curGroupIdx) != 1:
                  #  print(nxt, group[nxt], curGroupIdx, popped)
                    return -1, 0
                if nxt in group:
                    continue
                queue.append([nxt, curGroupIdx + 1])
                group[nxt] = curGroupIdx + 1        
        return res, len(group)