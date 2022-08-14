import copy
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        #build the graph
        modified_to_word = defaultdict(list)
        word_to_modified = defaultdict(list)
        for word in wordList:
            for i, char in enumerate(word):
                word_modified_by_one = word[:i] + '*' + word[i+1:]
                modified_to_word[word_modified_by_one].append(word)
                word_to_modified[word].append(word_modified_by_one)
        if endWord not in word_to_modified:
            return []        
        graph = defaultdict(set)
        if beginWord not in word_to_modified:
            for i, char in enumerate(beginWord):
                word_modified_by_one = beginWord[:i] + '*' + beginWord[i+1:]
                modified_to_word[word_modified_by_one].append(beginWord)
                word_to_modified[beginWord].append(word_modified_by_one)
            wordList.append(beginWord)
        for word in wordList:
            for modified in word_to_modified[word]:
                for nxt in modified_to_word[modified]:
                    graph[word].add(nxt)


        #Dijkstra
        distance = defaultdict(int)
        prev_nodes = defaultdict(set)
        visited = set()
        step = 0
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)
        while(queue):
            size = len(queue)
            step += 1
            for i in range(size):
                popped = queue.popleft()
                
                for nxt in graph[popped]:
                    if nxt in visited:
                        if step == distance[nxt]:
                            prev_nodes[nxt].add(popped)
                        continue
                    visited.add(nxt)
                    distance[nxt] = step
                    queue.append(nxt)
                    prev_nodes[nxt].add(popped)
        
        #search from endWord
        queue = deque()
        queue.append([endWord])
        res = []
        while(queue):
            size = len(queue)
            
            for i in range(size):
                popped = queue.popleft()
                last_word = popped[-1]
                if last_word == beginWord:
                    popped_reverse = popped[::-1]
                    res.append(popped_reverse)
                    continue
                for prev in prev_nodes[last_word]:
                    new_element = popped[:]
                    new_element.append(prev)
                    queue.append(new_element)
            if res:
                return res
        return res
        
            
        