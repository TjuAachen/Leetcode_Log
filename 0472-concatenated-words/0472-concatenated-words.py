class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        trie = defaultdict()
        word_key = '$'
        res = []
        words.sort(key = lambda x : len(x))
        
        
        for word in words:
            #find if curWord is a concatenated word
            if self.isPiecesInWords(word, 0, trie, defaultdict()):
                res.append(word)
            else:
                node = trie
                for char in word:
                    node = node.setdefault(char, {})
                node[word_key] = word
        
        return res
        
        
        
    def isPiecesInWords(self, curWord, start, trie, memo):
        
        if start in memo:
            return memo[start]
        
        res = False
        word_key = '$'
        node = trie
        n = len(curWord)
        
   
        if start == n:
            return True
        
        
        for i in range(start, n):
            curChar = curWord[i]

            if res:
                break
            if curChar in node:
                node = node[curChar]
            else:
                break
            
            if word_key in node:

                res |= self.isPiecesInWords(curWord, i + 1, trie, memo)
        
        memo[start] = res
        
        return res
        
                
        
        memo[start] = res
        
        return res
        
        

        
        
        
        