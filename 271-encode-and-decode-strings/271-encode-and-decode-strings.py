class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        def str2ascii(string):
            for char in string:
                asc = ord(char)
                cur = str(asc)
                while(len(cur) < 3):
                    cur = '0' + cur
                res.append(cur)
            res.append('256')
        for string in strs:
            str2ascii(string)
        return ''.join(res)
            
            
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        end = len(s) - 2
        i = 0
        res = []
        temp = []
        while(i < end):
            cur = s[i:i+3]
            if int(cur) < 256:
                temp.append(chr(int(cur)))
            else:
                res.append(''.join(temp[:]))
                temp = []
            i = i + 3
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))