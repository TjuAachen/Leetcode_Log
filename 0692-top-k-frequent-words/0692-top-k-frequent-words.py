class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        #input : a list of words
        #output : top K frequent elements, when frequency same, by lexical order
        #break down:
        #1. counter to find the frequency of each word
        #2. create a bucket and add each word into the trie tree at the corresponding index of the bucket ( frequency - 1)
        #3. traverse the bucket and get words from the trie tree.
        
        wordFreq = Counter(words)
        n = len(words)
        bucket = [{} for i in range(n)]
        
        for word, count in wordFreq.items():
            self.addWord(word, bucket[count - 1])
        ans = []
        self.k = k
        for i in range(n - 1, -1, -1):
            if bucket[i] and self.k > 0:
                self.getWord(ans, bucket[i])
        return ans
        
    def addWord(self, word, trie):
        node = trie
        wordKey = '$'
        for char in word:
            node = node.setdefault(char, {})
        node[wordKey] = word
    
    def getWord(self, res, node):
        if self.k <= 0:
            return
        if '$' in node:
            res.append(node['$'])
            self.k -=1
        for nxt in sorted(node.keys()):
            if nxt == '$':continue
            self.getWord(res, node[nxt])
        
        
        
        
        
        
        