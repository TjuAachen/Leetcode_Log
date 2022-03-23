class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums_sort = sorted(nums)
        n = len(nums)
        final = 0
        for i in range(n):
            left, right = i + 1, n - 1
            while(left < right):
                second, third = nums_sort[left], nums_sort[right]
                res = nums_sort[i] + second + third
                if res < target:
                    final += 1
                    left = left + 1
                    if left == right:
                        left = i + 1
                        right = right - 1
                else:
                    right = right - 1
                    left = i + 1
        return final
        