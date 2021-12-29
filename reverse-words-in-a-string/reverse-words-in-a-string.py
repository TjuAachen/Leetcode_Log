class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        word = ''
        s.strip()
        for i in s:
            if i != ' ':
                word = word + i
            else:
                if word != '':
                    if res != '':
                        res = word+' '+ res
                    else:
                        res = word
                    word = ''
        if word != '' and res != '':
            return word+' '+res
        elif word != '' and res == '':
            return word
        return res
                