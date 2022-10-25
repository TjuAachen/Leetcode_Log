class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.maxCommonLength(text1, text2, 0, 0, dict())
        
    def maxCommonLength(self, text1, text2, start1, start2, memo):
        if start1 == len(text1) or start2 == len(text2):
            return 0
        key = tuple([start1, start2])
        if key in memo:
            return memo[key]
        res = max(self.maxCommonLength(text1, text2, start1, start2 + 1, memo), self.maxCommonLength(text1, text2, start1 + 1, start2, memo))
        if text1[start1] == text2[start2]:
            res = max(res, self.maxCommonLength(text1, text2, start1 + 1, start2 + 1, memo) + 1)
        memo[key] = res
        return res
            
        