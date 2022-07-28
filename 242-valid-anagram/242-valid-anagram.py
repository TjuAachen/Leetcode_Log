class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_code_s = [0] * 26
        hash_code_t = [0] * 26
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False
        for i in range(s_len):
            cur_s = ord(s[i]) - ord('a') 
            cur_t = ord(t[i]) - ord('a')
            hash_code_s[cur_s] += 1
            hash_code_t[cur_t] += 1
        for i in range(26):
            if hash_code_s[i] != hash_code_t[i]:
                return False
        return True
        
        