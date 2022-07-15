from heapq import *
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if not edges:
            return [0]
        degree = [0] * n
        queue = deque()
        adj = defaultdict(list)
        for x, y in edges:
            degree[x] += 1
            degree[y] += 1
            adj[x].append(y)
            adj[y].append(x)
        height = []
        heapify(height)
        

        
        for i, deg in enumerate(degree):
            if deg == 1:
                queue.append(i)
                heappush(height, [0,i])
        
        cur_step = 0
        while(queue):
            size = len(queue)
            cur_step += 1
            for i in range(size):
                popped = queue.popleft()
                degree[popped] = 0
                for neighbor in adj[popped]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                        heappush(height, [-cur_step,neighbor])
        prev = None
        ans = []
        while(prev == None or (height and prev == height[0][0])):
            prev, ind = heappop(height)
            ans.append(ind)
        return ans
                        
        
                
        