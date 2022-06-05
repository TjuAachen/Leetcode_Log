class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        
        end = len(s)
        max_length = 0
        record = dict()
        while(right < end):
            #move the right pointer till two distinct letters
            while(right < end and (len(record) < 2 or (len(record) == 2 and s[right] in record)) ):
                if s[right] not in record:
                    record[s[right]] = 1
                else:
                    record[s[right]] += 1
                right += 1
            max_length = max(max_length, right - left)
            
            while(len(record) >= 2 and left < right):
                if record[s[left]] == 1:
                    del record[s[left]]
                else:
                    record[s[left]] = record[s[left]] - 1
                left += 1
        return max_length
            