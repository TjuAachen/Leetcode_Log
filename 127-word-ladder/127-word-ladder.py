from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        n = len(wordList)
        graph = dict()
        l = len(beginWord)
        for word in wordList:
            for i in range(l):
                if word[:i]+'*'+word[i+1:] not in graph:
                    graph[word[:i]+'*'+word[i+1:]] = set(word)
                graph[word[:i]+'*'+word[i+1:]].add(word)
        visited = {}
        length = 0
        queue = deque([beginWord])
        while(queue):
            size = len(queue)
            length += 1
            for i in range(size):
                popped = queue.popleft()
                visited[popped] = 1
                if popped == endWord:
                    return length
                for i in range(l):
                    z = popped[:i]+'*'+ popped[i+1:]
                    if z not in graph:
                        continue
                    for word in graph[z]:
                        if word not in visited:
                            queue.append(word)
        return 0

        