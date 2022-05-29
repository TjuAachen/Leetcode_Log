class Solution:
    def maxProduct(self, words: List[str]) -> int:
        binary = []
        def word2bin(word):
            ans = 0
            for char in word:
                if ans & (1<<(ord(char)-ord('a'))) == 0:
                    ans += 1<<(ord(char)-ord('a'))
            return ans
        for word in words:
            binary.append(word2bin(word))
        
        n = len(binary)
        res = 0
        for ind, num in enumerate(binary):
            for j in range(ind+1, n):
                if num & binary[j] == 0:
                    res = max(res, len(words[ind]) * len(words[j]))
        return res