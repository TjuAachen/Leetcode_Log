class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = 0
        for i in nums:
            middle = i
            cur_length = 1
            if middle in dic:
                del dic[middle]
            while( middle - 1 in dic ):
                cur_length += 1
                del dic[middle-1]
                middle = middle - 1
            middle = i
            while( middle + 1 in dic ):
                cur_length += 1
                del dic[middle + 1]
                middle = middle + 1
            res = max(res, cur_length)
        return res
            