class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        nums = ['0','1','6','8','9']
        mapping = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        nums_len = len(nums)
        res = []
        global temp
        temp = []
        def expand(temp, n):
            p = len(temp)
            last_half = []
            for i in range(p-1, -1, -1):
                last_half.append(mapping[temp[i]])
            if n%2 == 0:
                return temp+last_half, None, None
            else:
                return temp+['0']+last_half, temp+['1']+last_half,temp+['8']+last_half
        def permutation(number):
            global temp
            if len(temp) == (n // 2):
                res1, res2, res3 = expand(temp, n)
                if res1:
                    res.append(''.join(res1[:]))
                if res2 and res3:
                    res.append(''.join(res2[:]))
                    res.append(''.join(res3[:]))
                return
            for i in range(nums_len):
                if not temp and i == 0:
                    continue
                temp.append(nums[i])
                permutation(number + 1)
                temp.pop()
        permutation(0)
        return res
                
                
            