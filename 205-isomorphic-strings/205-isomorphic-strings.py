class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        mapping = dict()
        value = dict()
        if s_len != t_len:
            return False
        for i in range(s_len):
            key, val = s[i], t[i]
            if key in mapping and mapping[key] != val:
                return False
            if val in value and value[val] != key:
                return False
            mapping[key] = val
            value[val] = key
        return True
        