from sortedcontainers import SortedList
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count = 0
        
        
        properties.sort(reverse = True)
        
        defenseMax = []
        attackProperty = SortedList(key = lambda x: -x)
        
        i = 0
        for attack, defense in properties:
            if defenseMax and defenseMax[-1] < defense:
                defenseMax.append(defense)
            elif defenseMax:
                tmp = defenseMax[-1]
                defenseMax.append(tmp)
            else:
                defenseMax.append(defense)
            attackCount = attackProperty.bisect_left(attack)
            if attackCount > 0 and defenseMax[attackCount - 1] > defense:
                count += 1
            attackProperty.add(attack)
        return count
            
            
            
        
        
        
        