from sortedcontainers import SortedList
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        rank = dict()

        def dfs(node):
            global temp_cycle
            stack = []
            stack.append(node)
            count = 0
            rank[node] = 0
            seen.add(node)
            while(True):
               # print(rank)
                count += 1
                nxt = edges[node]
                if nxt == -1:
                    return
                
                #print(stack)
                if nxt not in rank and nxt not in seen:
                    rank[nxt] = count
                    stack.append(nxt)
                    node = nxt
                    seen.add(nxt)
                elif nxt in rank:
                    min_count = rank[nxt]                    
                    while(stack and rank[stack[-1]] >= min_count):
                        stack.pop()
                        temp_cycle += 1
                    return
                else:
                    return
                    
            return min(minimum, rank[node])
        global temp_cycle
        longest_cycle = - 1
        seen = set()
        for i, edge in enumerate(edges):
            if i not in seen and edge != -1:
                rank = dict()
                temp_cycle = 0
                dfs(i)
                if temp_cycle > 0:
                    longest_cycle = max(longest_cycle, temp_cycle)
        return longest_cycle
        
        
                    
                    
            
                