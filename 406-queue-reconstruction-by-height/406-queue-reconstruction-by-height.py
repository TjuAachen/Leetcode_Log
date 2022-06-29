from bisect import *
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        index_in_res = [i for i in range(n)]
        people.sort(key=lambda x:(x[0],-x[1]))
        res = [[0,0] for _ in range(n)]
        for h, k in people:
            if len(index_in_res) > 1:
                ind = index_in_res[k]
                res[ind][0], res[ind][1] = h, k
                index_in_res.pop(k)
            else:
                ind = index_in_res[-1]
                res[ind][0], res[ind][1] = h, k
                
        return res
        
                
            
        
        