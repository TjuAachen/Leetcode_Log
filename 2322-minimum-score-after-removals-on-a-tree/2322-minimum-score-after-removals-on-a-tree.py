from collections import deque
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        #for tree
        n = len(nums)
        graph = defaultdict(list)
        degree = [0] * n
        #graph generation
        for p1, p2 in edges:
            degree[p1] += 1
            degree[p2] += 1
            graph[p1].append(p2)
            graph[p2].append(p1)   
        
        #bfs
        xor = {}
        child = defaultdict(set)
        queue = deque()
        seen = set()
        total = 0
        for i in range(n):
            xor[i] = nums[i]
            total ^= nums[i]
            if degree[i] == 1:
                queue.append(i)
                seen.add(i)
                
                
        while(queue):
            popped = queue.popleft()
            for nxt in graph[popped]:
                if nxt in seen:
                    continue
                degree[nxt] -= 1
                child[nxt].add(popped)
                child[nxt] |= child[popped]
                xor[nxt] ^= xor[popped]
                if degree[nxt] == 1 and len(seen) != n:
                    seen.add(nxt)
                    queue.append(nxt)
        ans = float('inf')
        for i in range(n-1):
            for j in range(i+1, n - 1):
                p1, p2 = edges[i]
                p3, p4 = edges[j]
                if p2 in child[p1]: p1, p2 = p2, p1
                if p4 in child[p3]: p3, p4 = p4, p3
                
                if p1 in child[p3]:
                    left = xor[p1]
                    right = total^xor[p3]
                    middle = xor[p3] ^ left
                elif p3 in child[p1]:
                    left = xor[p3]
                    right = total^xor[p1]
                    middle = xor[p1] ^ left
                else:
                    left = xor[p1]
                    right = xor[p3]
                    middle = total^left^right
                cur = max([left,middle,right]) - min([left, right,middle])
                ans = min(cur, ans)
                if ans == 0:
                    return 0
        return ans
                
                
                    
                        
        
        