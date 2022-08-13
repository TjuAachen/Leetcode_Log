class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_freq = defaultdict(int)
        word_length = len(words[0])
        count_of_words = len(words)
        total_length = count_of_words * word_length
        
        #count the frequencies of words
        for word in words:
            word_freq[word] += 1
        
        res = []
      #  window_freq = defaultdict(int)
        for left_start in range(word_length):
            left = right = left_start
            diff = defaultdict(int)
            window_freq = defaultdict(int)
            while(right <= len(s) - word_length):
                new_word = s[right:right + word_length]
                right += word_length
                window_freq[new_word] += 1
                diff[new_word] += 1
                if diff[new_word] == 0:
                    del diff[new_word] 
                if right - left == total_length:
                    #make decisions
                    if left == left_start:
                        for word, freq in word_freq.items():
                            if word in window_freq:
                                diff[word] = window_freq[word] - freq
                            else:
                                diff[word] = - freq
                            if diff[word] == 0:
                                del diff[word]
                        if len(diff) == 0:
                            res.append(left)
                    else:
                       # print(diff,left, right)
                        if len(diff) == 0:
                            res.append(left)
                    #update left
                    old_word = s[left:left+word_length]
                    left += word_length
                    window_freq[old_word] -= 1
                    if window_freq[old_word] == 0:
                        del window_freq[old_word]
                    diff[old_word] -= 1
                    if diff[old_word] == 0:
                        del diff[old_word]
                   # print(left,old_word,  new_word, diff)
        return res
                
            
            
            
        
        
            
        