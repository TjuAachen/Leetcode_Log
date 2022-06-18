class WordFilter:

    def __init__(self, words: List[str]):
        self.record = dict()
        self.result = dict()
        for ind, word in enumerate(words):
            if word in self.record:
                self.record[word] = max(self.record[word], ind)
            else:
                self.record[word] = ind
            self.modify(word, ind)    
    def f(self, prefix: str, suffix: str) -> int:
        
        if (prefix, suffix) in self.result:
            return self.result[(prefix, suffix)]
        rolling_index = -1
        if (prefix, suffix) in self.record:
            rolling_index = self.record[(prefix, suffix)]
        self.result[(prefix, suffix)] = rolling_index
        return rolling_index
        
    def modify(self, word, index):
        n = len(word)
        
        for ind_i in range(n):
            for ind_j in range(n-1, -1, -1):
                remaining = 10 - n + ind_j - ind_i - 1
                prefix, suffix = word[:ind_i+1], word[ind_j:]
                if (prefix, suffix) in self.record:
                    self.record[(prefix, suffix)] = max(self.record[(prefix, suffix)], index)
                else:
                    self.record[(prefix, suffix)] = index
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)