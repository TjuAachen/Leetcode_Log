class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1,n2,n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False
        record = dict()
        def find(s1,s2,s3):
            if (len(s1) == 0 and s2 != s3) or (len(s2) == 0 and s1 != s3):
                record[(s1,s2,s3)] = False
                return False
            elif (len(s1) == 0 and s2 == s3) or (len(s2) == 0 and s1 == s3):
                record[(s1,s2,s3)] = True
                return True
            if (s1,s2,s3) in record:
                return record[(s1,s2,s3)]
            if s1[0] == s3[0] and s2[0] == s3[0]:
                res = (find(s1[1:],s2,s3[1:]) or find(s1,s2[1:],s3[1:]))
                record[(s1,s2,s3)] = res
                return res
            elif s1[0] == s3[0]:
                res = find(s1[1:],s2,s3[1:])
                record[(s1,s2,s3)] = res
                return res
            elif s2[0] == s3[0]:
                res = find(s1,s2[1:],s3[1:])
                record[(s1,s2,s3)] = res
                return res
            else:
                record[(s1,s2,s3)] = False
                return False
        return find(s1,s2,s3)
        