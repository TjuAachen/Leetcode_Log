class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_count = collections.Counter(magazine)
        ransom_count = collections.Counter(ransomNote)
        
        for i in range(26):
            cur = chr(i + ord('a'))
            x1 = magazine_count.setdefault(cur, 0)
            x2 = ransom_count.setdefault(cur, 0)
           # print(x1, x2, cur)
            if x1 < x2:
                return False
        return True