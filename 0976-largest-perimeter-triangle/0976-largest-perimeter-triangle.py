class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #sort
        nums.sort()
        ans = 0
        #find three numbers a <= b <= c such that a + b > c
        #traverse each number as the middle
        for i in range(1, len(nums) - 1):
            if self.isTriangle(nums[i-1:i+2]):
                ans = max(ans, sum(nums[i-1:i+2]))
        return ans
        
        
    def isTriangle(self, nums):
        a, b, c = nums
        if a + b > c:
            return True
        return False
        