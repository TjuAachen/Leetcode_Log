class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while(left+1 < right):
            mid = left + (right - left)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                # the mid is located at the left of the peak
                left = mid + 1
                
            
            elif arr[mid] < arr[mid-1]:
                # the mid is located at the right of the peak
                right = mid - 1
        if 0 <=left<= len(arr) - 1 and 0<=right <= len(arr)-1:
            if arr[left] == max(arr[left],arr[right]):
                return left
            else: 
                return right