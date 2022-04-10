import copy
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        n1, n2 = len(num1), len(num2)
        final = []
        def multiply(s1,s2, digit):
            res = []
            n = int(s2)
            tenth = 0 
            if n == 0 or s1[0] == "0":
                return ["0"]
            #s1 string, s2 char
            for i in range(len(s1)-1,-1,-1):
                temp =int(s1[i])*n + tenth
                tenth = temp//10
                unit = temp%10                    
                res = [str(unit)] + res
            for j in range(digit):
                res.append(str(0))
            if tenth > 0:
                res = [str(tenth)] + res
            return res
        def add(s1,s2):
            if not s1:
                return list(s2)
            if not s2:
                return list(s1)
            l1, l2 = len(s1),len(s2)
            long,short = max(l1,l2),min(l1,l2)
            if l1 == short:
                s1,s2 = s2,s1
                
            tenth = 0
            res = []
            for i in range(-1,-short-1,-1):
                temp = int(s1[i]) + int(s2[i]) + tenth
                tenth = temp // 10
                unit = temp%10
                res = [str(unit)] + res
            long_remain = copy.deepcopy(s1[:long-short])
            if tenth > 0:
                sub_res = add(long_remain, [str(tenth)])
            else:
                sub_res = long_remain
            res = sub_res + res
            return res
        digit = n1
        final = []
        for i in range(n1):
            m = int(num1[i])
            if digit == 0:
                temp = multiply(num2,str(m),0)
            else:
                temp = multiply(num2,str(m),digit-1)
                digit = digit - 1
            final = add(final, temp)
            
        return ''.join(final)
            
        