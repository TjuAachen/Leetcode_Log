class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set()
        for word in wordDict:
            words.add(word)
        self.memo = dict()    
        return self.isBreakable(s, 0, words)
           
    
    def isBreakable(self, s, start, words):
        if start == len(s):
            return True
        if start in self.memo:
            return self.memo[start]
        
        res =False
        for nxt in range(start, len(s) + 1):
            curStr = s[start : nxt]
            if curStr not in words:
                continue
            if self.isBreakable(s, nxt, words):
                self.memo[start] = True
                return True
        self.memo[start] = res
        return res
    
        