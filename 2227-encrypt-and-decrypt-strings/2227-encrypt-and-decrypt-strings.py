class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.keys = dict()
        self.values = dict()
        for index, char in enumerate(keys):
            self.keys[char] = values[index]   
        for index, char in enumerate(values):
            if char not in self.values:
                self.values[char] = [keys[index]]
            else:
                self.values[char].append(keys[index])
        self.dict = set(dictionary)
        

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        word1 = list(word1)
        def encry_word(word):
            for index, char in enumerate(word):
                if char in self.keys:
                    return self.keys[char]
                else:
                    return '1'
        for index, word in enumerate(word1):
            word1[index] = encry_word(word)
        return ''.join(word1)
    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        visited = dict()
        bundle = 0
        memoir = dict()
        
        for possible in self.dict:
            if self.encrypt(possible) == word2:
                bundle += 1
        return bundle
            
        
        
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)