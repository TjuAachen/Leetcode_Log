from collections import deque
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        #for tree
        n = len(nums)
        graph = dict()
        trace = dict()
        degree = [0] * n
        xor = dict()
        #graph generation
        for p1, p2 in edges:
            degree[p1] += 1
            degree[p2] += 1
            if p1 not in graph:
                graph[p1] = [p2]
            else:
                graph[p1].append(p2)
            if p2 not in graph:
                graph[p2] = [p1]
            else:
                graph[p2].append(p1)   
        
        #bfs
        queue = deque()
        visited = {}
        total = 0
        total_set = set()
        for i in range(n):
            xor[i] = nums[i]
            trace[i] = set()
            total ^= nums[i]
            total_set.add(i)
            if degree[i] == 1:
                queue.append(i)
                visited[i] = 1
        while(queue):
            popped = queue.popleft()
            for upper in graph[popped]:
                if upper in visited:
                    continue
                degree[upper] -= 1
                if degree[upper] == 1 and len(visited) != 1:
                    visited[upper] = 1
                    queue.append(upper)
                trace[upper].add(popped)
                trace[upper] |= trace[popped]
                xor[upper] ^= xor[popped]
        res = float('inf')
        for i in range(n-1):
            for j in range(i+1, n - 1):
                p1, p2 = edges[i]
                p3, p4 = edges[j]
                if p2 in trace[p1]: 
                    p1, p2 = p2, p1
                if p4 in trace[p3]: 
                    p3, p4 = p4, p3
                if p3 in trace[p1]:
                    left = xor[p3]
                    right = xor[p1] ^ left
                    middle = total ^ xor[p1]
                elif p1 in trace[p3]:
                    left = xor[p1]
                    right = xor[p3] ^ left
                    middle = total^xor[p3]
                else:
                    left = xor[p1]
                    right = xor[p3]
                    middle = total^left^right
                cur = max([left,right,middle]) - min([left, right,middle])
                res = min(res, cur)
                if res == 0:
                    return 0
        return res
                    
                        
        
        