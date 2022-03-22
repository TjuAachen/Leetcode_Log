class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        #add most a
        res = []
        cur = k
        rem = n
        for i in range(n):
            if (rem - 1)*26 >= cur - 1:
                res.append('a')
                rem = rem - 1
                cur = cur - 1
            else:
                break
        num_z = cur//26*['z']
        tran = ''
        if (cur%26) != 0:
            tran = chr((cur%26)+ord('a')-1)
        res.append(tran)
        res = res + num_z
        return ''.join(res)
                
            
        