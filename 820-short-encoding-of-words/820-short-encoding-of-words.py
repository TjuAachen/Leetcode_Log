class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        
        words = sorted(words, key = lambda x: -len(x))
        #generate suffix tree
        count = 0
        for ind, word in enumerate(words):
            cur = trie
            temp = reversed(word)
            is_included = True
            for ind_reversed, letter in enumerate(temp):
                if letter not in cur:
                    is_included = False
                    cur[letter] = {}
                cur = cur[letter]
            if not is_included:
                count += len(word) + 1
        return count