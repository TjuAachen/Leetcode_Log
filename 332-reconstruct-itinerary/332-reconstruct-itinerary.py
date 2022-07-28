from heapq import *
from sortedcontainers import SortedList
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        used_ticket = set()
        num_tickets = 0
        net_degree = defaultdict(int)
        adjacent = defaultdict(SortedList)
        #calculate the net degree, in degree -1, out degree +1
        for fr, arr in tickets:
            net_degree[fr] += 1
            net_degree[arr] -= 1
            num_tickets += 1
            adjacent[fr].add(arr)

        
   #     res = []
        #dfs to find the answer
  #      print(adjacent)
        def find_itinerary(airport, res):           
            while(adjacent[airport]):
                nxt = adjacent[airport].pop(0)
                find_itinerary(nxt, res)
            res.append(airport)
            #return False
        res = []
        find_itinerary('JFK', res)
        return res[::-1]
            
            
                
            
            
        
        
            
            
        