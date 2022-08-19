from heapq import *
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        end_subsequence = defaultdict(list)
        for num in nums:
            if end_subsequence[num-1]:
                prev_length = heappop(end_subsequence[num-1])
                heappush(end_subsequence[num], prev_length+1)
            else:
                heappush(end_subsequence[num], 1)
        return not any(queue and queue[0] < 3 for queue in end_subsequence.values())
        
        
        
        
        