class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        prefix = []
        for index, element in enumerate(arr):
            if index > 0:
                diff = arr[index] - arr[index-1]
                if diff == 0:
                    return False
                prefix.append(diff)
        peak = -1
        num_pos = [0]*(n-1)
        num_neg = [0]*(n-1)
        for index, i in enumerate(prefix):
            if index > 0:
                if i > 0:
                    num_pos[index] = num_pos[index-1] + 1
                    num_neg[index] = num_neg[index-1]
                else:
                    num_neg[index] = num_neg[index-1] + 1
                    num_pos[index] = num_pos[index-1]
                    if prefix[index-1] > 0 and prefix[index] < 0: 
                        peak = index - 1
            else:
                if i > 0:
                    num_pos[index] = 1
                    num_neg[index] = 0
                else:
                    return False
        if num_neg[peak] == 0 and num_pos[-1] - num_pos[peak] == 0 and num_neg[-1]>0:
            return True
        else:
            return False

                
            
                
        
        