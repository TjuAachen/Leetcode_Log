class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #input : an integer array
        #output : the sum of three integers such that the sum is closest to target
        #breaking down the problem:
        #1. select the first number, transform the original problem into a subproblem
        #2. finding the closest two sum to target - a1
        #3. repeat the process above until (n - 1)th integer is reached
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - 2):
            newTarget = target - nums[i]
            temp = self.findTwoSumClosest(nums, i + 1, newTarget)
            if temp + nums[i] == target:
                return target
            if abs(temp + nums[i] - target) < abs(res - target):
                res = temp + nums[i]
        return res
        
        
        
    
    def findTwoSumClosest(self, nums, start, target):
        n = len(nums)
        res = float('inf')
        left, right = start, n - 1
        while(left < right):
            ans = nums[left] + nums[right]
            if ans == target:
                return ans
            if ans < target:
                left += 1
            else:
                right -= 1
            if abs(target - ans) < abs(target - res):
                res = ans
        return res
        
        
        
                    

            
        