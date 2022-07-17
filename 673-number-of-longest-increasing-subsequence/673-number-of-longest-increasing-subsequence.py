class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        longest = [1] * n
        num_of_longest = [1] * n

        for i in range(n):
            cur_num = nums[i]
            for j in range(i):
                if nums[j] < cur_num:
                    if longest[i] <= longest[j]:
                        num_of_longest[i] = num_of_longest[j]
                    elif longest[i] == longest[j] + 1:
                        num_of_longest[i] += num_of_longest[j]
                    longest[i] = max(longest[i], longest[j] + 1)
        count = 0
        maximum_length = max(longest)
        for i in range(n):
            if longest[i] == maximum_length:
                count += num_of_longest[i]
        return count
                