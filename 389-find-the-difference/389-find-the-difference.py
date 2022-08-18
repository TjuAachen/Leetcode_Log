class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s, count_t = collections.Counter(s), collections.Counter(t)
        
        for i in range(26):
            cur_char = chr(ord('a') + i)
            s_count, t_count = 0, 0
            if cur_char in count_s:
                s_count = count_s[cur_char]
            if cur_char in count_t:
                t_count = count_t[cur_char]
            if s_count != t_count:
                return cur_char
            