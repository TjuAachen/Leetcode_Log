class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        size = [1]*n
        def find(x):
            while(x != parent[x]):
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return
            if rooty < rootx:
                parent[rootx] = rooty
                size[rooty] += size[rootx]
            else:
                parent[rooty] = rootx
                size[rootx] += size[rooty]                
        for pair in pairs:
            p1, p2 = pair[0], pair[1]
            union(p1,p2)
        region = dict()
        for i in range(n):
            root = find(i)
            if root not in region:
                region[root] = [i]
            else:
                region[root].append(i)
        s = list(s)
        for key,val in region.items():
            temp = []
            for m in val:
                temp.append(s[m])
            temp.sort()
            for i,m in enumerate(val):
                s[m] = temp[i]
        return ''.join(s)
            
        
                