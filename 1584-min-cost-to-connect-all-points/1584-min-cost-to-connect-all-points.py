class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        include = set()
        n_node = 0
        cur = 0
        final = 0
        n = len(points)
        min_inc = [10**7]*n
        min_inc[0] = 0
        while(n_node < n):
            min_cost = 10**7
            for i in range(n):
                if i not in include and min_inc[i]<min_cost:
                    nxt = i
                    min_cost = min_inc[i]
            include.add(nxt)
            final += min_cost
            n_node += 1
            #update
            for i in range(n):
                distance = abs(points[i][0]-points[nxt][0])+abs(points[i][1]-points[nxt][1])
                min_inc[i] = min(min_inc[i],distance)
        return final
        