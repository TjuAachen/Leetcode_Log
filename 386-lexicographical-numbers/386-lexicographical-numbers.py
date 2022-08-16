class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        
        def dfs(start):
            if start > n:
                return
            res.append(start)
            for i in range(10):
                dfs(start*10+i)
        
        for start in range(1, 10):
            if start > n:
                continue
            dfs(start)
        return res

            
            
            
            