class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        count_1 = 0
        p_nums1, p_nums2 = 0, 0
        while( p_nums1 < m + n and p_nums2 < n):
            if nums1[p_nums1] > nums2[p_nums2]:
                nums1.insert(p_nums1, nums2[p_nums2])
                nums1.pop()
                p_nums2 += 1
            p_nums1 += 1
        if p_nums2 < n:
            nums1[-(n-p_nums2):]= nums2[p_nums2:n]

        