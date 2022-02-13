class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        record = dict()
        res = 0
        while(right < len(s)):
            if s[right] not in record:
                record[s[right]] = 1
            else:
                record[s[right]] += 1
            while(len(record.keys()) > k and left <= right):
                record[s[left]] = record[s[left]] - 1
                if record[s[left]] == 0:
                    del record[s[left]]
                left = left + 1
            res = max(res, right-left+1)
            right = right + 1
        return res
        