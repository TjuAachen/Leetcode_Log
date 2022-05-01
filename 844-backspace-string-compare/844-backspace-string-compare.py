class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s, t = s[::-1], t[::-1]
        i, j = 0, 0
        skips, skipt = 0, 0
        while(i < len(s) or j < len(t)):
            while(i < len(s)):
                if s[i] == '#':
                    skips += 1
                    i = i + 1
                elif skips > 0:
                    skips = skips -1
                    i = i + 1
                else:
                    break
            while(j < len(t)):
                if t[j] == '#':
                    skipt += 1
                    j = j + 1
                elif skipt > 0:
                    skipt = skipt - 1
                    j = j + 1
                else:
                    break
            if i < len(s) and j < len(t) and s[i] != t[j]:
                return False
            if (i == len(s) and j < len(t)) or (i < len(s) and j == len(t)):
                return False
            i = i + 1
            j = j + 1
            
        return True
                