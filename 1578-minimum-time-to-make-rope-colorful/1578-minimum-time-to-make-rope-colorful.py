from heapq import * 
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        #need to be removed
        
        left = 0
        #sliding window
        n = len(colors)
        ans = 0
        while(left < n):
            if left + 1 < n and colors[left + 1] == colors[left]:
                right = left
                heap = []
                while(right < n and colors[right] == colors[left]):
                    heappush(heap, neededTime[right])
                    right += 1
                while(len(heap) > 1):
                    ans += heappop(heap)
                left = right
            else:
                left += 1
        return ans
                
                
                
        