class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_len = len(nums)
        def quickSelect(l, r, pivot):
            j = l
            for i in range(l, r + 1):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j = j + 1
            nums[j], nums[pivot] = nums[pivot], nums[j]
            return j
        def find(l, r):
            if l == r == nums_len - k:
                return nums[l]
            newPivot = quickSelect(l,r-1, r)
            if newPivot == nums_len - k:
                return nums[newPivot]
            elif newPivot > nums_len - k:
                return find(l, newPivot - 1)
            else:
                return find(newPivot+1, r)
        return find(0, len(nums) - 1)
        