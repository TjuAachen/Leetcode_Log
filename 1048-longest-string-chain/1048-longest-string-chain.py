from collections import deque
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        graph = dict()
        wordsNum = len(words)
        
        outDeg = [0] * wordsNum
        memoir = {}
        def is_predecessor(word1, word2):
            word1Len, word2Len = len(word1), len(word2)
            if word2Len - word1Len != 1:
                return False
            for i in range(word2Len):
                removed_word = word2[:i] + word2[i+1:]
                if removed_word == word1:
                    return True
            return False
        
        for i, word in enumerate(words):
            for j in range(wordsNum):
                if i == j:
                    continue
                if is_predecessor(word, words[j]):
                    if words[j] not in graph:
                        graph[words[j]] = [word]
                    else:
                        graph[words[j]].append(word)
                    outDeg[i] += 1
        def longest_chain(root):
            queue = deque()
            queue.append(root)
            step = 0
            while(queue):
                size = len(queue)
                step += 1
                for i in range(size):
                    popped = queue.popleft()
                    if popped not in memoir:
                        memoir[popped] = step
                    else:
                        if step <= memoir[popped]:
                            continue
                        else:
                            memoir[popped] = max(memoir[popped], step)
                    cur_node = popped
                    if cur_node not in graph:
                        continue
                    for prev in graph[cur_node]:
                        queue.append(prev)
            return step
        res = 0
        for i,degree in enumerate(outDeg):
            if degree == 0:
                res = max(longest_chain(words[i]), res)
        return res
        
            
                
        