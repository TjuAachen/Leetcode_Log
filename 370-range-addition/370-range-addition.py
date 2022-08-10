class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff_array = [0] * length
        
        for start, end, val in updates:
            diff_array[start] += val
            if end + 1 < length:
                diff_array[end + 1] -= val
        
        arr = [0] * length
        arr[0] = diff_array[0]
        #print(diff_array)
        for i in range(1, length):
            arr[i] = arr[i-1] + diff_array[i]
        return arr
                    
                    
        
        