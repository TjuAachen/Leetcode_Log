class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #bfs
        valToIdx = defaultdict(set)
        for idx, num in enumerate(arr):
            valToIdx[num].add(idx)
        
        visited = set()
        n = len(arr)
        #[idx, step]
        queue = deque([[0, 0]])
        visited.add(0)
     #   visitedVal.add(arr[0])
        
        
        while (queue):
            poppedIdx, curStep = queue.popleft()

            if poppedIdx == n - 1:
                return curStep
            
            #nxt
            if poppedIdx - 1 >= 0 and poppedIdx - 1 not in visited:
                queue.append([poppedIdx - 1, curStep + 1])
                visited.add(poppedIdx - 1)
            if poppedIdx + 1 < n and poppedIdx + 1 not in visited:
                queue.append([poppedIdx + 1, curStep + 1])
                visited.add(poppedIdx + 1)
            for nxt in valToIdx[arr[poppedIdx]]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append([nxt, curStep + 1])
            valToIdx[arr[poppedIdx]] = set()
        
        return -1
                