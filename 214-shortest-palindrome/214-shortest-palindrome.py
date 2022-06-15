class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = s + '#' + s[::-1]
        if len(s) <= 1:
            return s
        new_sNum = len(new_s)
        nxt = [0] * new_sNum
        j = 0
        i = 1
        while(i < new_sNum):
            if new_s[i] == new_s[j]:
                nxt[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                nxt[i] = 0
                i += 1
            else:
                j = nxt[j-1]
        return s[nxt[-1]:][::-1] + s
                
            
            
        