class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        start = 1
        ans = 0
        for i, num in enumerate(nums):
            if k == 0:
                return ans
          #  print(i, num, start, k, 1)
            if num != start:
                curNum = min(k, num - start)
                ans += (start + start + curNum - 1) * curNum // 2
                k -= curNum
                start = start + curNum + 1
            else:
                start = num + 1
        return ans + (nums[-1] + 1 + nums[-1] + k) * k //2