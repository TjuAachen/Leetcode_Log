class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = dict()
        KEY = '$'
        for ind, word in enumerate(words):
            n = len(word)
            for i in range(n, -1, -1):
                suffix = word[i:]
                new_word = suffix + '#' + word
                cur = self.trie
                cur[KEY] = ind
                for letter in new_word:
                    cur = cur.setdefault(letter, {})
                    cur[KEY] = ind
                
    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            else:
                cur = cur[letter]
        return cur['$']
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)