class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        res = []
        i = 0
        length = len(s)
        
        while(i < length):
            tempCount = 0
            j = i
            while(j < length and s[j] == s[i]):
                tempCount += 1
                j += 1
            res.append(str(tempCount))
            res.append(s[i])
            i = j
        return ''.join(res)
            