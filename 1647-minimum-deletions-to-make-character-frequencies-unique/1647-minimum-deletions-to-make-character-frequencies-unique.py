class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_freq = defaultdict(int)
        
        for char in s:
            word_freq[char] += 1
        
        freq_count = defaultdict(int)
        
        for key, val in word_freq.items():
            freq_count[val] += 1
        res = 0
        frequency = list(freq_count.keys())
        frequency.sort(reverse = True)
      #  print(freq_count)
        max_frequency = frequency[0]
        for freq in range(max_frequency, 0, -1):
            count = freq_count[freq]
           # print(count, freq)
            if count > 1:
               # print(count)
                freq_count[freq-1] += count - 1
                res += count - 1
        return res        
        