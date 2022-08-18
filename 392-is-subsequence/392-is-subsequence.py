class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        p = 0
        if s == '':
            return True
        for char in t:
            cur_s = s[p]
            if char == cur_s:
                p += 1
            if p == s_len:
                return True
        return False
        