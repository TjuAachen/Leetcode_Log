class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        res = 0
        while(left <= right):
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            min_h = min(max_left, max_right)
            if max_left == min_h:
                res += min_h - height[left]
                left = left + 1
            else:
                res += min_h - height[right]
                right = right - 1
        return res
        