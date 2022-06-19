class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.cache = dict()
        self.words = dict()
        for ind, word in enumerate(wordsDict):
            if word in self.words:
                self.words[word].append(ind)
            else:
                self.words[word] = [ind]
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]
        if (word2, word1) in self.cache:
            return self.cache[(word2, word1)]
        list1, list2 = self.words[word1], self.words[word2]
        n_list1, n_list2 = len(list1), len(list2)
        node2 = 0
        res = float('inf')
        for elem in list1:
            while(node2 < n_list2 and list2[node2] < elem):
                res = min(res, elem - list2[node2])
                node2 += 1
            if node2 != n_list2:
                res = min(res,  list2[node2] - elem)
            else:
                res = min(res,  elem - list2[-1])
                break
        self.cache[(word1, word2)] = res
        self.cache[(word2, word1)]= res
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)