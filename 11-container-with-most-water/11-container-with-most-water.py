class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height) - 1
        left, right = 0, end
        area = 0
        while(left < right):
            cur = min(height[left], height[right])
            area = max(area, cur*(right-left))
            if height[left] == cur:
                while(left<right and height[left] <= cur):
                    left = left + 1
            else:
                while(left<right and height[right] <= cur):
                    right = right - 1
            
        return area
                