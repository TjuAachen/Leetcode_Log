class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sort = sorted(nums)
        n = len(nums_sort)
        diff = 10**5
        for i in range(n):
            left, right = i+1, n - 1
            while(left < right):
                second, third = nums_sort[left], nums_sort[right]
                cur = nums_sort[i] + second + third
                diff_cur = abs(target-cur)
                if cur == target:
                    return target
                if diff_cur < diff:
                    diff = diff_cur
                    res = cur 
                if cur < target:
                    left = left + 1
                else:
                    right = right - 1
        return res
                    

            
        