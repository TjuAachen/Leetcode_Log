class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = [0]*len(s)
        i = 0
        while(i < len(s)):
            if(i == 0 or s[i] != s[i-1]):
                count[i] = 1
            else:
                count[i] = count[i-1] + 1
                if count[i] == k:
                    s = s[:i-k+1] + s[i+1:]
                    i = i - k
            i += 1
        return s
        
            
        
        