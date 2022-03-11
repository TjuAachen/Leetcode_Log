class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        left, right = 1, n - 1
        while(left < n and arr[left]>arr[left-1]):
            left = left + 1
        while(right > 0 and arr[right] < arr[right-1]):
            right = right - 1
        if left >=n or right<=0 or arr[left] >= arr[left-1] or arr[right] <= arr[right-1]:
            return False
        elif right == left - 1:
            return True
        else:
            return False
        
    
        