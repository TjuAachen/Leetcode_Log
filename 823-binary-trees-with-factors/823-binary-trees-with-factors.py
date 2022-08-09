class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        pairs = defaultdict(list)
        
        arr.sort()
        
        n = len(arr)
        leaf = set()
        arr_set = set(arr)
        for i in range(n-1, -1, -1):
            cur = arr[i]
            visited = set()
            for j in range(i, -1, -1):
                nxt = arr[j]
                if cur%nxt == 0:
                    another = cur // nxt
                    if another in arr_set and another not in visited:
                        pairs[cur].append((nxt, another))
                        visited.add(another)
                        visited.add(nxt)
            if cur not in pairs:
                leaf.add(cur)
        memo = {}
       # print(pairs)
        def count_from_root(node):
            if node in memo:
                return memo[node]
            if node in leaf:
                memo[node] = 1
                return 1
            ans = 0
            for factor1, factor2 in pairs[node]:
                if factor1 == factor2:
                    ans += count_from_root(factor1) * count_from_root(factor1) 
                else:
                    ans += count_from_root(factor1)*count_from_root(factor2)*2
            memo[node] = ans + 1
            return memo[node]
        
        ans = 0
        
        for num in arr:
            temp = count_from_root(num)
            ans = (ans+temp)%(10**9 + 7)
          #  print(ans, num, temp)
        #print(memo)
        return ans%(10**9+7)
        
            
                        
                        
        
        
            
        