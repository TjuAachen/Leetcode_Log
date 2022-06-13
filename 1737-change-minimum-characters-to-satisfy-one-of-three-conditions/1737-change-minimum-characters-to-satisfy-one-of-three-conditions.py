from collections import Counter
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        #firstly, select the possible ones
        def str2dict(string):
            res = [0] * 26
            min_char = 25
            max_char = 0
            for char in string:
                ind = ord(char) - ord('a')
                res[ind] += 1
                min_char = min(min_char, ind)
                max_char = max(max_char, ind)
            return res, min_char, max_char
        res_a, min_a, max_a = str2dict(a)
        res_b, min_b, max_b = str2dict(b)
        
        def sub_sum(res_a):
            res = [0] * 27
            for i in range(26):
                res[i + 1] = res[i] + res_a[i]
            return res
        
        prefix_a = sub_sum(res_a)
        prefix_b = sub_sum(res_b)
        
        if max_a < min_b or min_a > max_b or len(res_a) == len(res_b) == 1:
            return 0
        res = float('inf')
        #strategy 3:
        for i in range(26):
            if res_a[i] != 0 and res_b[i] != 0:
                temp_a = prefix_a[i] + prefix_a[-1] - prefix_a[i+1]
                temp_b = prefix_b[i] + prefix_b[-1] - prefix_b[i+1]
                res = min(res, temp_a + temp_b)

        #a > b
        def num_step(prefix_a, prefix_b, min_a, min_b, max_a, max_b):
            temp = float('inf')
            #str1 < str2
            for i in range(max_b + 1):
                cur = i
                #for b
                    
                if cur >= min_b:
                    if cur == 25 and max_b == 25:
                        temp_b = prefix_b[max_b + 1] - prefix_b[cur]
                    else:
                        temp_b = prefix_b[max_b + 1] - prefix_b[cur + 1]
                else:
                    temp_b = prefix_b[max_b + 1] - prefix_b[cur]
                #for a
                if cur < min_a:
                    temp_a = 0
                else:
                    temp_a = prefix_a[cur + 1] - prefix_a[min_a]
                temp = min(temp, temp_a + temp_b)
            return temp
        res_ab = num_step(prefix_a, prefix_b, min_a, min_b, max_a, max_b)
        res_ba = num_step(prefix_b, prefix_a, min_b, min_a, max_b, max_a) 
        
        res = min([res, res_ab, res_ba])
        return res
                    
                    


                
        
        
        
            
                    