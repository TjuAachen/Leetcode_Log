class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_array = [0] * 26
        for word in words2:
            temp = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                temp[index] += 1
            for i in range(26):
                word2_array[i] = max(word2_array[i], temp[i])
        res = []
        for word in words1:
            temp = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                temp[index] += 1
            flag = False
            for i in range(26):
                if word2_array[i] > temp[i]:
                    flag = True
                    break
            if not flag:
                res.append(word)
        return res