class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        count = []
        slow = 0
        s = list(s)
        for fast in range(n):
            s[slow] = s[fast]
            if(slow == 0 or s[slow] != s[slow-1]):
                count.append(1)
            else:
                count[-1] += 1
                if count[-1] == k:
                    count.pop()
                    slow = slow - k
            slow += 1
        return ''.join(s[:slow])
            
            
        
            
        
        