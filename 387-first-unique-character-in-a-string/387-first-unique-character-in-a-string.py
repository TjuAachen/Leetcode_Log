class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.Counter(s)
        
        for ind, char in enumerate(s):
            if char in freq and freq[char] == 1:
                return ind
        return -1
        
        
        
        