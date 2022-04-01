class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        nxt = [-1]*len(nums2)
        for ind, num2 in enumerate(nums2):
            while stack and num2 > nums2[stack[-1]]:
                nxt[stack[-1]] = num2
                stack.pop()
            stack.append(ind)
        ans = [-1]*len(nums1)
        for index, num1 in enumerate(nums1):
            ans[index] = nxt[nums2.index(num1)]
        return ans
        