class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #backtracking + trie tree
        trie = defaultdict()
        self.buildTrie(words, trie)
        
        res = []
        #starting from different points
        nrow, ncol = len(board), len(board[0])

        
        for i in range(nrow):
            for j in range(ncol):
                self.backtracking(board, trie, i, j, res)
        
        return res

    def buildTrie(self, words, trie):
        
        word_key = '$'
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[word_key] = word
    

    def backtracking(self, board, parent, x, y, word_matched):
        
        nrow, ncol = len(board), len(board[0])
        curChar = board[x][y]
        
        #termination condition
        if curChar not in parent:
            return
        
        currentNode = parent[curChar]
        
        #check if we find a match of word
        wordKey = '$'
        word_match = currentNode.pop(wordKey, False)
        if word_match:
            word_matched.append(word_match)
        
        #mark board[x][y] as visited
        board[x][y] = '#'
        
        
        #explore the neighbors in 4 directions, i.e. up, right, down, left
        for diffX, diffY in [(1,0), (0,1),(-1,0),(0,-1)]:
            nxtX, nxtY = x + diffX, y + diffY
            if nxtX < nrow and nxtX >= 0 and nxtY < ncol and nxtY >= 0 and board[nxtX][nxtY] in currentNode:
                self.backtracking(board, currentNode, nxtX, nxtY, word_matched)
        
        #End of exploreation, we restore the cell
        board[x][y] = curChar
        
        #optimization : incrementally remove the matched leaf node in Trie
        if not currentNode:
            del parent[curChar]


        