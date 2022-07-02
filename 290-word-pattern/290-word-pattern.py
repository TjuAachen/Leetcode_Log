class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = s.split(' ')
        mapping_pos = {}
        mapping_neg = {}
        if len(strings) != len(pattern):
            return False
        for char,string in zip(pattern,strings):
            if char not in mapping_pos:
                mapping_pos[char] = string
            elif mapping_pos[char] != string:
                return False
            if string not in mapping_neg:
                mapping_neg[string] = char
            elif mapping_neg[string] != char:
                return False
        return True