from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        record = dict()
        def check(s1,s2):
            if s1 == s2:
                return True
            if (s1,s2) in record:
                return record[(s1,s2)]
            if len(s1) != len(s2):
                return False
            d1, d2 = Counter(s1), Counter(s2)
            for key,val in d1.items():
                if d2[key] != val:
                    record[(s1,s2)] = False
                    return record[(s1,s2)]
            final = []
            for i in range(len(s1)-1):
                sub1_s1, sub2_s1 = s1[:i+1], s1[i+1:]
                sub1_s2, sub2_s2 = s2[:i+1], s2[i+1:]
                back1_s2, back2_s2 = s2[:(len(s2)-i-1)], s2[(len(s2)-i-1):]
                if check(sub1_s1,sub1_s2) and check(sub2_s1,sub2_s2):
                    record[(s1,s2)] = True
                    return record[(s1,s2)]
                elif check(sub2_s1,back1_s2) and check(sub1_s1,back2_s2):
                    record[(s1,s2)] = True
                    return record[(s1,s2)]
            record[(s1,s2)] = False
            return record[(s1,s2)]
        return check(s1,s2)
                
            
        