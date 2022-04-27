class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        #build the graph
        graph = dict()
        for pair in pairs:
            p1, p2 = pair[0], pair[1]
            if p1 not in graph:
                graph[p1] = [p2]
            else:
                graph[p1].append(p2)
            if p2 not in graph:
                graph[p2] = [p1]
            else:
                graph[p2].append(p1)
        #dfs find the connected region
        n = len(s)
        visited = dict()
        def dfs(vertex):
            if vertex in visited:
                return
            visited[vertex] = 1
            track.append(vertex)
            if vertex in graph:
                nxt = graph[vertex]
            else:
                nxt = []
            for i in nxt:
                dfs(i)
            return
        region = []
        for i in range(n):
            track = []
            dfs(i)
            if len(track) > 0:
                track.sort()
                region.append(track)
        s = list(s)
        for conn in region:
            temp = []
            for m in conn:
                temp.append(s[m])
            temp.sort()
            for i, m in enumerate(conn):
                s[m] = temp[i]
        return ''.join(s)
        
        