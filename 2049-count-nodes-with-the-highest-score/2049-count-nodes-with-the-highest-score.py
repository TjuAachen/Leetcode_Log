class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        #generate adjacency list of the graph
        n = len(parents)
        graph = {}
        for i in range(n):
            parent = parents[i]
            if parent != -1:
                if i in graph:
                    graph[i].append(parent)
                else:
                    graph[i] = [parent]
                if parent in graph:
                    graph[parent].append(i)
                else:
                    graph[parent] = [i]
        #generate count of nodes under a root
        count = {}
        def dfs(root, parent):
            if root in count:
                return count[root]
            temp = 0
            for child in graph[root]:
                if child == parent:
                    continue
                temp += dfs(child, root)
            count[root] = temp + 1
            return count[root]
        for i in range(n):
            if i in count:
                continue
            dfs(i, parents[i])
        def score(i):
            res = 1
            if i == 0:
                for child in graph[i]:
                    res *= count[child]
            else:
                for child in graph[i]:
                    if child != parents[i]:
                        res *= count[child]
                res *= (n - count[i])
            return res
        ans = -float('inf')
        record ={}
        for i in range(n):
            cur = score(i)
            ans = max(ans, cur)
            if cur in record:
                record[cur] += 1
            else:
                record[cur] = 1
        return record[ans]
            
        
        