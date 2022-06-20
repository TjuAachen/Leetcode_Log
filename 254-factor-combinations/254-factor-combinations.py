import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        factor = []
        upper = math.sqrt(n)
        i = 2
        while(i <= upper):
            if (n%i == 0):
                if (n//i == i):
                    factor.append(i)
                else:
                    factor.extend([i,int(n//i)])
            i = i + 1
        if not factor:
            return []
        final = []
        res = []
        global temp
        temp = n
        factor_len = len(factor)
        def find_factor(start):
            global temp
            if temp == 1:
                final.append(res[:])
                return
            for f in range(start, factor_len):
                cur_f = factor[f]
                if temp % cur_f != 0:
                    continue
                temp = temp // factor[f]
                res.append(factor[f])
                find_factor(f)
                res.pop()
                temp = temp * factor[f]
        find_factor(0)
        return final