class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        n = len(s)
        record = dict()
        max_length = 0
        while(left < n):
            cur = s[right]
            right_index = ord(cur) - ord('a')
            
            while(right < n and right_index not in record):
                record[right_index] = 1
                right += 1
                if right == n:
                    return max(max_length, right - left)
                cur = s[right]
                right_index = ord(cur) - ord('a')
            max_length = max(max_length, right - left)
            
            while(left < right and s[left] != cur):
                cur_left = s[left]
                cur_index = ord(cur_left) - ord('a')
                del record[cur_index]
                left += 1
            left = left + 1
            del record[right_index]
        return max_length 
            
            
            
        