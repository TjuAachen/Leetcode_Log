class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def res(n):
            final = []
            if n == 1:
                return "1"
            middle = list(res(n-1))
            m = len(middle)
            i = 0
            while(i < m):
                val = middle[i]
                count = 0
                while(i < m and middle[i] == val):
                    i = i + 1
                    count = count + 1
                final += [str(count), val]
                
            return "".join(final)
        return res(n)
        