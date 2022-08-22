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
        shorter.append(float('inf'))
        shorter.insert(0, -float('inf'))
        longer.append(float('inf'))
        longer.insert(0, -float('inf'))        
        target_k = (longer_len + shorter_len) // 2
        
        if shorter_len == 0:
            if longer_len%2:
                return longer[target_k+1]
            return (longer[target_k] + longer[target_k+1])/2.0
        

        def binary_search(left, right):
            while(left <= right):
                mid = left + (right - left) // 2
             #   print(left, right, mid, target_k)
                shorter_idx = target_k + 1 - mid
              #  print(shorter_idx,shorter[shorter_idx])
                if shorter_idx < 1:
                    right = mid - 1
                    continue
                if shorter_idx > shorter_len:
                    left = mid + 1
                    continue
                if shorter[shorter_idx - 1]<= longer[mid] <= shorter[shorter_idx + 1]:
                    return mid, shorter_idx, True
                if longer[mid - 1] <= shorter[shorter_idx] <= longer[mid + 1]:
                    return mid, shorter_idx, False
                if longer[mid] < shorter[shorter_idx - 1]:
                    left = mid + 1
                if longer[mid] > shorter[shorter_idx + 1]:
                    right = mid - 1
        left, right = 0, longer_len 
        longer_idx, shorter_idx, in_longer = binary_search(left, right)
        is_odd = (longer_len + shorter_len) % 2
        longer_val, shorter_val = longer[longer_idx], shorter[shorter_idx]
       # print(longer_idx, shorter_idx)
        if in_longer:
            #k//2
            if longer_val >= shorter_val:
                if is_odd:
                    return longer_val
                return (max(longer[longer_idx - 1], shorter_val) + longer_val)/2.0
            #k/2 - 1
            if is_odd:
                return min(longer[longer_idx + 1], shorter_val)
            return (min(longer[longer_idx + 1], shorter_val) + longer_val)/2.0
        #k//2
        if longer_val <= shorter_val:
            if is_odd:
                return shorter_val
            return (max(longer[longer_idx - 1], shorter[shorter_idx - 1]) + shorter_val)/2.0
        #k/2 - 1
        if is_odd:
            return min(longer[longer_idx + 1], shorter[shorter_idx + 1])
        return (min(longer[longer_idx + 1], shorter[shorter_idx + 1]) + shorter_val)/2.0 
                
        
            
            
        
            
            
                     
                     
        
        