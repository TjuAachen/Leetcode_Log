class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        total = 0
        while(left < right):
            min_height = min(height[left], height[right])
            total = max((right - left )*min_height,total)
            if min_height == height[left]:
                left = left + 1
            else:
                right = right - 1
        return total
        