class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        candidate1, candidate2 = -1, -1
        res = float('inf')
        if word1 != word2:
            for ind, elem in enumerate(wordsDict):
                if elem == word1:
                    candidate1 = ind
                if elem == word2:
                    candidate2 = ind
                if candidate1 != -1 and candidate2 != -1:
                    res = min(res, abs(candidate1 - candidate2))
        
        else:
            for ind, elem in enumerate(wordsDict):
                if elem == word1:
                    if candidate1 == -1:
                        candidate1 = ind
                    elif candidate2 == -1:
                        candidate2 = ind
                        res = min(res, abs(candidate2 - candidate1))
                    else:
                        candidate1, candidate2 = candidate2, candidate1
                        candidate2 = ind
                        res = min(res, abs(candidate2 - candidate1))
        return res

                
        