class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_unique = len(set(s))
        n = len(s)
        res = 0
        for cur_unique in range(1, max_unique + 1):
            #sliding_window
            count = defaultdict(int)
            left, right = 0, 0
            while(right < n):
                count[s[right]] += 1
                right += 1
                if min(count.values()) >= k:
                    res = max(res, right - left)
                while(left < right and len(count) > cur_unique):
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
        return res
        
        
            
            
            
        