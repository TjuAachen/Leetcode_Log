class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowHash = defaultdict(int)
        deleted = 0
        curLongest = 0
        ans = 0
        n = len(s)
        left, right = 0, 0
        while(right < n):
            curChar = s[right]
            right += 1
            windowHash[curChar] += 1
            deleted = right - left - max(windowHash.values())
            while(left < right and deleted > k):
                leftChar = s[left]
                left += 1
                windowHash[leftChar] -= 1
                deleted = right - left - max(windowHash.values())
            curLongest = right - left
            ans = max(curLongest, ans)
        return ans
        
        