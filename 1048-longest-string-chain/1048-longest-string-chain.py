from collections import deque
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        score = dict()
        words = sorted(words, key = lambda x: len(x))
        final = 0
        for word in words:
            cur_length = 0
            for i in range(len(word)):
                removed_word = word[:i] + word[i+1:]
                previousLength = score.setdefault(removed_word, 0)
                cur_length = max(previousLength + 1, cur_length)
            score[word] = cur_length
            final = max(cur_length, final)
        return final
            
            
        
        
            
                
        