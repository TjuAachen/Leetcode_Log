class Solution(object):
    def is_exist(self, start, cur_sum, matchsticks, step, onPath):
        global side_length, visited
        if cur_sum > side_length:
            return False
        if cur_sum == side_length and step < 3:
            return self.is_exist(0,0, matchsticks, step+1, set())
        if cur_sum == side_length and step == 3:
            return True
        for i in range(start, len(matchsticks)):
            if i in visited:
                continue
            if i > 0 and i - 1 not in visited and i - 1 not in onPath and matchsticks[i-1] == matchsticks[i]:
                continue
            onPath.add(i)
            visited.add(i)
            temp = self.is_exist(i+1, cur_sum + matchsticks[i],matchsticks, step, onPath)
            if temp:
                return True
            onPath.remove(i)
            visited.remove(i)
        return False
        
        
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        global side_length, visited
        total_sum = sum(matchsticks)
        if total_sum%4 != 0:
            return False
        
        side_length = total_sum // 4
        matchsticks.sort()
        visited = set()
        return self.is_exist(0, 0, matchsticks, 0, set())
        
        
                
            
                
        
        