from heapq import *
class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = Counter(words)
        heap = []        
        for word, count in wordFreq.items():
            if len(heap) == k and (heap[0].freq < count or (heap[0].freq == count and heap[0].word > word)):
                heappop(heap)
                heappush(heap, Pair(word, count))
            elif len(heap) < k:
                heappush(heap, Pair(word, count))
        res = []
        
        while(heap):
            popped = heappop(heap)
            res.append(popped.word)
        return res[::-1]
        
        
        