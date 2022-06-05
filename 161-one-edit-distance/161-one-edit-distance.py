class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        len_s, len_t = len(s), len(t)
        i = 0
        #insert
        if len_s - len_t == -1:
            while(i < len(s)):
                if i < len_t and s[i] != t[i]:
                    return s[i:] == t[i+1:]
                i = i + 1
            return True
        #replace
        if len_s - len_t == 0:
            while(i < len(s)):
                if i < len_t and s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
                i = i + 1
        #delete
        if len_s - len_t == 1:
            while(i < len(s)):
                if i < len_t and s[i] != t[i]:
                    return s[i+1:] == t[i:]
                i = i + 1
            return True
        return False
                
        