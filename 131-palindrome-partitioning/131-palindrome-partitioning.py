class Solution:
    def partition(self, s: str) -> List[List[str]]:
        global total, res
        total = []
        res = []
        def is_palindrome(string):
            left, right = 0, len(string) - 1
            while(left < right):
                if string[left] != string[right]:
                    return False
                else:
                    left += 1
                    right = right - 1
            return True
        length = len(s)
        def dfs(s):
            if len(s) == 0:
                total.append(res[:])
                return
            for i in range(len(s)):
                substring = s[:(i+1)]
                if is_palindrome(substring):
                    res.append(substring)
                    dfs(s[(i+1):])
                    res.pop()
        dfs(s)
        return total
            