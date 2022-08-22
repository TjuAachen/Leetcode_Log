class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        longer, shorter = nums1, nums2
        longer_len, shorter_len = len(longer), len(shorter)
        longer.insert(0, -float('inf'))
        longer.append(float('inf'))
        shorter.insert(0, -float('inf'))
        shorter.append(float('inf'))
        
        left, right = 1, shorter_len + 1
        
        target_k = (shorter_len + longer_len) // 2
        is_odd = (shorter_len + longer_len)%2
       # print(left, right)
        while(left <= right):
            
            mid = left + (right - left) // 2
            longer_idx = target_k - mid + 2
            shorter_left = shorter[mid - 1]
            longer_left = longer[longer_idx - 1]
        #    print(left, right, mid)
            if max(shorter_left, longer_left) <= min(shorter[mid], longer[longer_idx]):
                if is_odd:
                    return min(shorter[mid], longer[longer_idx])
                return (max(shorter_left, longer_left)+min(shorter[mid], longer[longer_idx]))/2.0
            elif shorter_left > longer[longer_idx] :
                right = mid - 1
            elif shorter[mid] < longer_left:
                left = mid + 1
                
            
            
            
                
        
            
            
        
            
            
                     
                     
        
        