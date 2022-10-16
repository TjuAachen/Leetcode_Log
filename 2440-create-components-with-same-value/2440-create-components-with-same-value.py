class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        #build tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        #bfs
        def contribute(cur, parent):
            ans = nums[cur]
            for nxt in tree[cur]:
                if nxt != parent:
                    ans += contribute(nxt, cur)
            if ans == cand:
                return 0
            return ans
        total = sum(nums)
        for cand in range(1, total//2 + 1):
            if total%cand == 0 and contribute(0, -1) == 0:
                return total // cand - 1
        return 0
            
        