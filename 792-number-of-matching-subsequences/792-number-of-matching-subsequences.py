from bisect import *
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        record = defaultdict(list)
        for i, char in enumerate(s):
            record[char].append(i)
        count = 0
        for word in words:
            start = 0
            flag = True
            temp = defaultdict(int)
            for char in word:
                n = len(record[char])
                cur_n = n - temp[char]
                if cur_n <= 0:
                    flag = False
                    break
                index = bisect_left(record[char], start, temp[char], n)
                if index == n:
                    flag = False
                    break
                start = record[char][index] + 1
                temp[char] = index + 1
            if flag:
                count += 1
        return count