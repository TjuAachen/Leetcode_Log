import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = dict()
        freq2num = dict()
        freq = []
        for num in nums:
            if num not in num2freq:
                num2freq[num] = 1
            else:
                num2freq[num]+= 1
        for key in num2freq.keys():
            freqval = num2freq[key]
            freq.append(freqval)
            if freqval not in freq2num:
                freq2num[freqval] = [key]
            else:
                freq2num[freqval].append(key)
        heapq.heapify(freq)
        res = heapq.nlargest(k,freq)
        final = []
        for ele in res:
            final.append(freq2num[ele].pop())
        return final
            
        
                
        