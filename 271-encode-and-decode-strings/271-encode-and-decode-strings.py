class Codec:
    
    def str_to_int(self, byte_str):
        res = 0
        for num in byte_str:
            res = res * 256 + ord(num)
        return res
    def len_to_str(self,x):
        x = len(x)
        bytes = [chr(x<<(i*8)&0xff) for i in range(4)]
        bytes.reverse()
        return ''.join(bytes)
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)    

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        i = 0
        output = []
        while(i < n):
            len_str = s[i:i+4]
            length = self.str_to_int(len_str)
            i += 4
            output.append(s[i:i+length])
            i += length
        return output
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))