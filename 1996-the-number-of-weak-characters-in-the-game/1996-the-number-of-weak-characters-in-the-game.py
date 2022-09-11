from sortedcontainers import SortedList
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count = 0
        
        
        properties.sort(reverse = True, key = lambda x:(x[0],-x[1]))
        
        maxDefense = 0
        i = 0
      #  print(properties)
        for attack, defense in properties:
            if maxDefense > defense:
                count+= 1
            maxDefense = max(maxDefense, defense)
        return count
            
            
            
        
        
        
        