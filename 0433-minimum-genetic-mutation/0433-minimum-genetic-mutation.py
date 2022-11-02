class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        validGenes = set(bank)
        
        neighbors = defaultdict(list)
        
        if end not in validGenes:
            return -1
        for gene in bank:
            self.buildDict(gene, validGenes, neighbors)
        self.buildDict(start, validGenes, neighbors)
        
        
        queue = deque([start])
        size = 0
        visited = set([start])
        step = 0
        while(queue):
            size = len(queue)
            for i in range(size):
                popped = queue.popleft()
                if popped == end:
                    return step
                for nxt in neighbors[popped]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            step += 1
        return -1
            
        
        
    def buildDict(self, start, validGenes, neighbors):
        for i, char in enumerate(start):
            for mutated in "AGTC":
                if mutated != char:
                    temp = start[:i] + mutated + start[i+1:]
                    if temp in validGenes:
                        neighbors[start].append(temp)
                        neighbors[temp].append(start)
        