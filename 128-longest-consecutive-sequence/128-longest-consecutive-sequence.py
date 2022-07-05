class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #intelligently built subsequence
        num_set = set(nums)
        
        longest_streak = 0
        for num in nums:
            if num - 1 not in num_set:
                cur_elem = num
                cur_streak = 0
                while cur_elem in num_set:
                    cur_streak += 1
                    cur_elem += 1
                longest_streak = max(longest_streak, cur_streak)
        return longest_streak
                
            