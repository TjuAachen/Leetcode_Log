from collections import *
class Solution:
    def minDeletions(self, s: str) -> int:
        hash_array = [0] * 26
        for char in s:
            hash_code = ord(char) - ord('a')
            hash_array[hash_code] += 1
        
        min_val = float('inf')
        deleted = 0
        hash_array.sort()
        i = 0
        while(i < 26 and hash_array[i] == 0):
            i = i + 1
        hash_array_modified = hash_array[i:]
        
        distinct = []
        freq_of_num = defaultdict(int)
        for i, elem in enumerate(hash_array_modified):
            freq_of_num[elem] += 1
            if not distinct or elem != distinct[-1]:
                distinct.append(elem)
        
        distinct = [0] + distinct
        end = len(distinct)
        global res, temp
        res = float('inf')
        temp = 0
        def dfs(i):
            global res, temp
            if i == 0:
                res = min(res, temp)
                return
            num_of_gaps = distinct[i] - distinct[i-1] - 1
            elems_to_arrange = freq_of_num[distinct[i]] - 1
            if elems_to_arrange == 0:
                dfs(i-1)
                return
            able_to_arrange = min(num_of_gaps, elems_to_arrange) 
            unable_to_arrange = elems_to_arrange - able_to_arrange
            temp += (able_to_arrange + 1)*able_to_arrange//2
            if unable_to_arrange == 0:
                dfs(i-1)
                temp -= (able_to_arrange + 1)*able_to_arrange//2
                return
            #unable to arrange then reduce to 0
            temp += unable_to_arrange * distinct[i]
            dfs(i-1)
            temp -= unable_to_arrange * distinct[i]
            #unable to arrange, then reduce to previous elems
            temp += unable_to_arrange * (distinct[i] - distinct[i-1])
            freq_of_num[distinct[i-1]] += unable_to_arrange
            dfs(i-1)
            freq_of_num[distinct[i-1]] -= unable_to_arrange
            temp -= unable_to_arrange * (distinct[i] - distinct[i-1])
            temp -= (able_to_arrange + 1)*able_to_arrange//2
            return
        dfs(end-1)
        return res