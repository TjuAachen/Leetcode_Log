class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sort = sorted(nums)
        def findTwo(first, index):
            left, right = index+1, len(nums_sort) - 1
            diff = 10**5
            while(left < right):
                second, third = nums_sort[left], nums_sort[right]
                cur = first + second + third
                diff_cur = abs(target-cur)
                if cur == target:
                    return target
                if diff_cur < diff:
                    diff = diff_cur
                    res = cur 
                if left+1 == right:
                    return res
                if cur < target:
                    left = left + 1
                else:
                    right = right - 1
        n = len(nums)
        diff = 10**5
        for i in range(n):
            if i <= n - 3:
                cur = findTwo(nums_sort[i],i)
                diff_cur = abs(target-cur)
                if cur == target:
                    return target
                if diff_cur < diff:
                    diff = diff_cur
                    res = cur
        return res