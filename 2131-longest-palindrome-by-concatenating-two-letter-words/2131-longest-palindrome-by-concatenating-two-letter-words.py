class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordFreq = Counter(words)
        ans = 0
        center = False
        for word, wordCount in wordFreq.items():
            if word[0] == word[1]:
                if wordCount % 2 == 0:
                    ans += wordCount
                else:
                    ans += wordCount - 1
                    center = True
            elif word[0] > word[1]:
                ans += min(wordCount, wordFreq[word[1] + word[0]]) * 2
        if center:
            ans += 1
        return ans * 2

                
                
        