from math import *
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        num_str = str(num)
        n = len(num_str)
        num2word = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
        ten2word={10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        
        def str2word(string):
            num = int(string)
            res = []
            hundred = num//100
            if hundred > 0:
                res.append(num2word[hundred])
                res.append('Hundred')
            num_from_ten = (num - hundred*100)
            if 10 <= num_from_ten < 20:
                res.append(ten2word[num_from_ten])
            else:
                ten = num_from_ten // 10
                if ten > 0:
                    res.append(ten2word[ten*10])
                
                digit = (num_from_ten - ten*10)
                if digit > 0:
                    res.append(num2word[digit])
            return ' '.join(res)
        i = n
        final = []
        count2unit = {0:None,1:'Thousand',2:'Million',3:'Billion'}
        count = 0
        while(i - 3 >= 0):
            cur = num_str[i-3:i]
            temp = str2word(cur)
            if count2unit[count] and temp:
                final = [temp] + [count2unit[count]] + final
            elif temp:
                final = [temp] + final
            i = i - 3
            count += 1
        if i > 0:
            remaining = num_str[:i]
            temp = str2word(remaining)
            if count2unit[count]:
                final = [temp] + [count2unit[count]] + final
            else:
                final = [temp]  + final
        return ' '.join(final)
            
            
            