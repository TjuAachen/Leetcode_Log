class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_array = defaultdict(int)
        for word in words2:
            temp = defaultdict(int)
            for char in word:
                temp[char] += 1
                word2_array[char] = max(word2_array[char], temp[char])
        res = []
        for word in words1:
            temp = defaultdict(int)
            for char in word:
                temp[char] += 1
                
            flag = False
            for key in word2_array.keys():
                if word2_array[key] > temp[key]:
                    flag = True
                    break
            if not flag:
                res.append(word)
        return res