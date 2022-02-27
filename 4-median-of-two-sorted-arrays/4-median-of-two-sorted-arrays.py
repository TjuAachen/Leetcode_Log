class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        flag = (m + n) % 2
        k = (n + m -1) // 2
        res = []
        if m == 0:
            if flag == 1:
                return nums2[k]
            return (nums2[k] + nums2[k+1]+0.0)/2
        if n == 0:
            if flag == 1:
                return nums1[k]
            return (nums1[k] + nums1[k+1]+0.0)/2
        if m == min(m,n):
            nums1, nums2 = nums2, nums1
        nums2 = [-10**6-1] + nums2 + [10**6 + 1]
        nums1 = [-10**6-1] + nums1 + [10**6 + 1]
        left, right = 1, len(nums2) - 2
        while(left <= right):
            mid = left + (right - left) // 2 
            ele_middle = k - mid + 2
            if nums1[ele_middle] == nums2[mid]:
                return nums2[mid]
            elif nums1[ele_middle] < nums2[mid]:
                if nums2[mid] <= nums1[ele_middle+1]:
                    if flag == 1:
                        return max(nums1[ele_middle],nums2[mid-1])
                    else:
                        return (max(nums1[ele_middle],nums2[mid-1]) + nums2[mid]+0.0)/2
                else:
                    right = mid -1
            else:
                if nums1[ele_middle] <= nums2[mid+1]:
                    if flag == 1:
                        return max(nums2[mid], nums1[ele_middle-1])
                    else:
                        return (nums1[ele_middle] + max(nums1[ele_middle-1],nums2[mid])+0.0)/2
                else:
                    left = mid + 1
            if right == 0:
                if flag == 1:
                    return nums1[k+1]
                return (nums1[k+1]+nums1[k+2]+0.0)/2
            if left == len(nums2)-1:
                if flag == 1:
                    return nums1[k+1-n]
                return (nums1[k+1-n]+nums1[k+2-n]+0.0)/2
            
                     
                     
        
        