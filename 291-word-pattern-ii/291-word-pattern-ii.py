class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pattern2s = {}
        s2pattern = {}
        global res
        res = False
        def dfs(pattern, s):
            global res
            if not pattern and not s:
                res = True
                return
            if not pattern or not s:
                return
            n = len(s)
            for i in range(n):
                string = s[:i+1]
                pattern_one = pattern[0]
                if pattern_one in pattern2s and pattern2s[pattern_one] != string:
                    continue
                if string in s2pattern and s2pattern[string] != pattern_one:
                    continue
                pattern_flag = False
                string_flag = False
                if pattern_one in pattern2s:
                    pattern_flag = True
                if string in s2pattern:
                    string_flag = True
                pattern2s[pattern_one] = string
                s2pattern[string] = pattern_one
                dfs(pattern[1:], s[i+1:])
                if not string_flag:
                    del s2pattern[string]
                if not pattern_flag:
                    del pattern2s[pattern_one]
        dfs(pattern, s)
        
        return res
        