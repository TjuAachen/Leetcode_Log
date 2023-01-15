class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular) + 1
        costExpress = [0] * n
        costRegular = [0] * n
        costExpress[0] = expressCost
        ans = [0] * (n - 1)
        
        for idx in range(1, n):
            costRegular[idx] = min([costRegular[idx - 1] + regular[idx - 1], costExpress[idx - 1] + regular[idx - 1], costExpress[idx - 1] + express[idx - 1]])
            costExpress[idx] = min([costExpress[idx - 1] + express[idx - 1], costRegular[idx - 1] + regular[idx - 1] + expressCost, costRegular[idx - 1] + expressCost + express[idx - 1]])
            
            ans[idx - 1] = min(costRegular[idx], costExpress[idx])
        
        return ans
        
            
            
        