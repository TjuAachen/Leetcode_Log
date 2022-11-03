class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        pairCount, isRemaining = self.countSymmetricPairs(words)
        extra = 0
        if isRemaining:
            extra = 2
     #   print(pairCount, extra)
        return pairCount * 4 + extra
        
        
    def countSymmetricPairs(self, words):
        count = 0
        wordFreq = Counter(words)
        isRemaining = False
        sameWords = set()
        for i, word in enumerate(words):
            symmetricOne = word[1] + word[0]
            if symmetricOne == word:
                sameWords.add(word)
            if symmetricOne == word and word in wordFreq and wordFreq[word] >= 2:
                wordFreq[word] -= 2
                count += 1
                if wordFreq[word] == 0:
                    del wordFreq[word]
            elif symmetricOne != word and symmetricOne in wordFreq and word in wordFreq:
                wordFreq[symmetricOne] -= 1
                wordFreq[word] -= 1
                count += 1
                if wordFreq[symmetricOne] == 0:
                    del wordFreq[symmetricOne]
                if wordFreq[word] == 0:
                    del wordFreq[word]
        for word in sameWords:
            if word in wordFreq:
                return count, True
        return count, False

                
                
        