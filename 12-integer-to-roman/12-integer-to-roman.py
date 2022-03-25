class Solution:
    def intToRoman(self, num: int) -> str:
        record ={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        thousand = num // 1000
        hundred = (num // 100)%10
        ten = (num // 10)%10
        indiv = num%10
        final = []
        final += ["M"]*(thousand)
        def transform(final, digit,value):
            upper = 5*value
            upmost = upper*2
            if 3<digit <=5:
                final += ([record[value]]*(5-digit)+[record[upper]])
            elif digit <= 3:
                final += [record[value]]*digit
            elif 9 > digit > 5:
                final += [record[upper]]+[record[value]]*(digit-5)
            else:
                final += [record[value]]+ [record[upmost]]
        transform(final,hundred, 100)
        transform(final,ten, 10)
        transform(final,indiv,1)
        return ''.join(final)
        
        
                
            
            