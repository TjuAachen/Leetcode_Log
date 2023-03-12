class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        #find the maximum left ascending array
        left = 0
        n = len(arr)
        right = n - 1
        
        left = self.findBoundary(arr, left)
        right = self.findBoundary(arr, right)
 
        if (left >= right):
            return 0
        
        j = right
        res = right
        for i in range(left + 1):
            leftVal = arr[i]
            while (j < n and arr[j] < leftVal):
                j += 1
            res = min(res, j - i - 1)
        
        return res
        
    
    def findBoundary(self, arr, start):
        step = 1
        if start == len(arr) - 1:
            step = -1
        while (start + step < len(arr) and start + step >= 0 and (-step)* arr[step + start] <= arr[start] * (-step)):
            start += step
        
        return start