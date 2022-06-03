class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        global res, final
        res = []
        final = []
        
        def find_sentence(s):
            if s == '':
                final.append(' '.join(res))
                return
            length = len(s)
            for i in range(length):
                substring = s[:(i+1)]
                if substring in wordDict:
                    res.append(substring)
                    find_sentence(s[(i+1):])
                    res.pop()
            return
        find_sentence(s)
        return final
        