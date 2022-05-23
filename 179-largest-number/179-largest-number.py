class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for ind, num in enumerate(nums):
            nums[ind] = str(num)
        nums.sort()
        nums.reverse()
        res = []
        n = len(nums)
        for ind, char in enumerate(nums):
            if ind < n - 1:
                max_comb = char + nums[ind+1]
                max_ind = ind
                for j in range(ind+1,n):
                    if nums[j] + char > max_comb:
                        max_comb = nums[j] + char
                        max_ind = j
                nums[ind], nums[max_ind] = nums[max_ind], nums[ind]
                res.append(nums[ind])
            else:
                res.append(nums[ind])
        #remove extra 0s
        if res[0] == '0':
            res = ['0']
        return ''.join(res)
        