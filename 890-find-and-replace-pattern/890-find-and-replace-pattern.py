class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            word_to_pattern = {}
            pattern_to_word = {}
            flag = False
            for i, char in enumerate(word):
                if char not in word_to_pattern:
                    word_to_pattern[char] = pattern[i]
                elif pattern[i] != word_to_pattern[char]:
                    flag = True
                    break
                if pattern[i] not in pattern_to_word:
                    pattern_to_word[pattern[i]] = char
                elif pattern_to_word[pattern[i]] != char:
                    flag = True
                    break
            if not flag:
                res.append(word)
        return res
            
                
        