class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        result = 0
        has_odd = False
        for count in counts.values():
            if count % 2 == 0:
                result += count
            else:
                has_odd = True
                result += count - 1
        if has_odd:
            result += 1
        return result

        