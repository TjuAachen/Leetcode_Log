class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
      #  con_set = set()
        combine = []
        for i in range(n):
            for j in range(i+1,n):
                combine.append((i,j))
        def distance(x):
            point1, point2 = points[x[0]], points[x[1]]
            return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
        combine.sort(key = lambda x: distance(x))
        count = 0
        final = 0
        parent = [i  for i in range(n)]
        def find(x):
            while(x != parent[x]):
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return
            parent[rootx] = rooty   
        for conn in combine:
            p1, p2 = conn[0], conn[1]
            if count == n - 1:
                return final
            if find(p1) != find(p2):
                final += distance(conn)
                count += 1
                union(p1,p2)
        return final