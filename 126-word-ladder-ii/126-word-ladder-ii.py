from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        aster2word = {}
        isExist = False
        for word in wordList:
            if word == endWord:
                isExist = True
            for ind, char in enumerate(word):
                temp = word[:ind] + '*' + word[ind+1:]
                if temp not in aster2word:
                    aster2word[temp] = [word]
                else:
                    aster2word[temp].append(word)
        if not isExist:
            return []
        def adj(word):
            res = set()
            for ind, char in enumerate(word):
                temp = word[:ind] + '*' + word[ind+1:]
                if temp in aster2word:
                    res = res.union(set(aster2word[temp]))
            return list(res)
        queue = deque()
        queue.append([beginWord])
        final = []
        min_length = float('inf')
        memoir = {}
        while(queue):
            size = len(queue)
            for _ in range(size):
                popped = queue.popleft()
                #popped is a subsequence with the last element as the most recent one
                most_recent = popped[-1]
                adjacent = adj(most_recent)
                length = len(popped)                    
                for nxt in adjacent:
                    if nxt not in memoir:
                        memoir[nxt] = length + 1
                    elif length + 1 > memoir[nxt]:
                        continue
                    if nxt == endWord:
                        popped.append(nxt)
                        final.append(popped[:])
                        popped.pop()
                    else:
                        popped.append(nxt)
                        queue.append(popped[:])
                        popped.pop()
        return final
        
                
                    
                