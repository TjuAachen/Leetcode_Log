class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2num = {'I':1, 'V':5,'X':10,'L':50, 'C':100,'D':500, 'M':1000}
        pairs = {'I':['V', 'X'], 'X':['L', 'C'], 'C':['D', 'M']}
        i = 0
        s_len = len(s)
        res = 0
        for i, char in enumerate(s):
            if char in pairs and i < s_len - 1 and s[i+1] in pairs[char]:
                res -= roman2num[char]
            else:
                res += roman2num[char]
        return res
            
                    
        