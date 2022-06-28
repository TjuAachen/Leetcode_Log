from collections import *
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        def compare(word1, word2):
            i, j = 0, 0
            word1_len, word2_len = len(word1), len(word2)
            while(i < word1_len and j < word2_len and word1[i] == word2[j]):
                i += 1
                j += 1
            prev, cur = None, None
            if i < word1_len:
                prev = word1[i]
            if j < word2_len:
                cur = word2[j]
            return prev, cur
        
        hash_array = [0] * 26
        graph = defaultdict(list)
        degree = defaultdict(int)
        for i, word in enumerate(words):
            for char in word:
                hash_code = ord(char) - ord('a')
                if hash_array[hash_code] == 0:
                    hash_array[hash_code] = 1
            if i > 0:
                prev, cur = compare(words[i-1], word)
                if prev and cur:
                    graph[prev].append(cur)
                    degree[cur] += 1
                    graph[cur]
                    hash_code1 = ord(prev) - ord('a')
                    hash_code2 = ord(cur) - ord('a')
                    hash_array[hash_code1] = -1
                    hash_array[hash_code2] = -1
                if prev and not cur:
                    return ""
        queue = deque()
        res = []
        seen = {}
        for key, val in graph.items():
            if degree[key] == 0:
                queue.append(key)
                seen[key] = 1
                res.append(key)
        n = len(graph)
        #topological sorting
        while(queue):
            popped = queue.popleft()
            for nxt in graph[popped]:
                degree[nxt] -= 1
                if degree[nxt] == 0 and len(seen) < n:
                    queue.append(nxt)
                    seen[nxt] = 1
                    res.append(nxt)
        if len(seen) == n:
            for i, num in enumerate(hash_array):
                if num == 1:
                    cur = chr(i+ord('a'))
                    res.append(cur)
            return ''.join(res)
        return ""
                
                
        
        
                        
                        
                
                    
        