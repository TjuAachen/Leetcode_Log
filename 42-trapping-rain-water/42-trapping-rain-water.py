class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = height[0], height[len(height) - 1]
        left, right = 0, len(height) - 1
        res = 0
        while(left <= right):
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
                left_max = max(left_max,height[left])
            else:
                res += right_max - height[right]
                right = right - 1
                right_max = max(right_max,height[right])
        return res
        