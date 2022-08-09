class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        pairs = defaultdict(list)
        
        arr.sort()
        
        n = len(arr)
       # leaf = set()
      #  n = len(arr)
        MOD = 10**9 + 7
        memo =defaultdict(lambda: 1)
        #dp = [1] * n
        arr_set = set(arr)
        for i in range(n):
            cur = arr[i]
            memo[cur]
            for j in range(i):
                nxt = arr[j]
                another = cur // nxt
                if cur%nxt == 0 and another in arr_set:
                    memo[cur] += (memo[nxt] * memo[another])%MOD
                        
        
        return sum(list(memo.values()))%MOD
        

        
            
                        
                        
        
        
            
        