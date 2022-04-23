class Codec:    
    record = dict()
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = 1
    def getString(self):
        c = Codec.num
        res = []
        while(c > 0):
            c = c - 1
            res.append(Codec.chars[c%62])
            c = c//62
        return ''.join(res)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = self.getString()
        res = "http://tinyurl.com/" + code
        Codec.num = Codec.num + 1
        Codec.record[code] = longUrl
        return res
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.replace("http://tinyurl.com/",'')
        longUrl = Codec.record[code]
        return longUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))