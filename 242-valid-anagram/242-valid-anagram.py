class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        if s == t:
            return True
        return False
        