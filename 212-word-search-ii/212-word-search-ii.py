class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nrow, ncol = len(board), len(board[0])
        
        #construct trie tree for words
        trie = dict()
        
        word_key = '$'
        
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[word_key] = word
        
        #dfs search in the trie tree of words
        res = []
        diff = [(0,1),(0,-1),(1,0),(-1,0)]
        def backtracking(i,j,node):
            letter = board[i][j]
            if letter in node:
                board[i][j] = '#'
                if word_key in node[letter]:
                    res.append(node[letter][word_key])
                    del node[letter][word_key]
             #   nxt_board = defaultdict(list)
                for dx, dy in diff:
                    newx, newy = dx + i, dy + j
                    if 0 <= newy < ncol and 0 <= newx < nrow and board[newx][newy] !='#':
                        backtracking(newx, newy, node[letter])
                board[i][j] = letter
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] not in trie:
                    continue
              #  visited = set()
                backtracking(i, j, trie)
        return res
                
            
        