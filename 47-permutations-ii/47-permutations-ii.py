class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        used = dict()
        n = len(nums)
        result, track = [], []
        def generate(step):
            if step == n :
                result.append(track[:])
                return
            for i in range(n):
                if i > 0 and nums[i-1] == nums[i] and i-1 not in used:
                    continue
                if i in used:
                    continue
                track.append(nums[i])
                used[i] = 1
                generate(step+1)
                del used[i]
                track.pop()
        generate(0)
        return result