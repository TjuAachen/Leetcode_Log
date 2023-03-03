class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #KMP
        n = len(haystack)
        m = len(needle)
        
        if n < m:
            return -1
        
        #maximum length of overlapping prefix and suffix 
        prevPos = [0] * m
 
        for i in range(1, m):
            j = i

            while (j > 0):
                if needle[prevPos[j - 1]] == needle[i]:
                    prevPos[i] = prevPos[j - 1] + 1
                    break
                j = prevPos[j - 1]
           
            if j == 0:
                prevPos[i] = 0

        strP = 0
        targetP = 0

        while (strP < n):
            
            # start matching
        #    print(targetP, strP, '1')
            while (targetP < m and strP < n and needle[targetP] == haystack[strP]):
                targetP += 1
                strP += 1
         #   print(targetP, strP, '2')
            if targetP == m:
                return strP - m
            if targetP != 0:
                targetP = prevPos[targetP - 1]
            else:
                strP += 1
        
        return -1
                
                
                
        
        
        
        