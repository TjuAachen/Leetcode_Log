from heapq import * 
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        char_freq = Counter(s)
        heap = []
        res = []
     #   temp = []
        for char, freq in char_freq.items():
            heappush(heap, [-freq, char])
        
        while(heap):
            temp = []
            maximum = 1
            while(heap and len(temp) < k):
                popped = heappop(heap)
                #print(popped, heap)
                maximum = max(-popped[0], maximum)
                res.append(popped[-1])
                temp.append(popped)
            if len(temp) < k and maximum > 1:
                return ''
            while(temp):
                popped = temp.pop()
                new_freq_vec = [popped[0] + 1, popped[1]]
                if new_freq_vec[0] != 0:
                    heappush(heap, new_freq_vec)
        return ''.join(res)
                
                
        
        
        
            
            
            
        
        