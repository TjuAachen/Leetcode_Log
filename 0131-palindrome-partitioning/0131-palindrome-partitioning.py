class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.n = len(s)
        self.isPalindrome = [[True] * self.n for _ in range(self.n)]
        
        for start in range(self.n - 1, -1, -1):
            curStart = s[start]
            for end in range(start, self.n):
                curEnd = s[end]
                if start == end:
                    continue
                if start + 1 == end:
                    self.isPalindrome[start][end] = curStart == curEnd
                    continue
                self.isPalindrome[start][end] = self.isPalindrome[start + 1][end - 1] and curStart == curEnd
        res = []
        self.divide(s, 0, [], res)
        
        return res
                
    def divide(self, s, start, curAns, res):
        if start == self.n:
            res.append(curAns[:])
            return
        
        for nxt in range(start, self.n):
            curSubstring = s[start : nxt+1]
            if self.isPalindrome[start][nxt]:
                curAns.append(curSubstring)
                self.divide(s, nxt + 1, curAns, res)
                curAns.pop()
        
        
        