class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()
        def count(s):
            if s in record:
                return record[s]
            if len(s) <= 1:
                record[s] = len(s)
                return len(s)
            for i in range(len(s)-1):
                if s[i] == s[-1]:
                    m1 = count(s[i+1:len(s)-1])
                    m2 = count(s[:len(s)-1])
                    if m1 == max(m1+2,m2):
                        record[s[i+1:len(s)-1]] = m1 + 2
                    else:
                        record[s[:len(s)-1]] = m2
                    record[s] = max(m1+2,m2)
                    return record[s]
            record[s] = count(s[:len(s)-1])
            return record[s]
        return count(s)
                    