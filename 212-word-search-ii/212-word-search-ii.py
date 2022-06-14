class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        rowNum = len(board)
        colNum = len(board[0])
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        #keep words with trie
        #backtrack along the trie
        #remove the traversed from the trie
        matched_words = []
        diff = [(0,1), (0,-1),(1,0),(-1,0)]
        def dfs(row, col, parent):
            letter = board[row][col]
            cur_node = parent[letter]
            
            word_match = cur_node.pop(WORD_KEY, False)
            
            if word_match:
                matched_words.append(word_match)
            
            #revisited
            board[row][col] = '#'
            
            for row_offset, col_offset in diff:
                newRow, newCol = row + row_offset, col + col_offset
                if 0 <= newRow < rowNum and 0 <= newCol < colNum and board[newRow][newCol] in cur_node:
                    dfs(newRow, newCol, cur_node)
            
            board[row][col] = letter
            
            #remove leaf node
            if not cur_node:
                parent.pop(letter)
        
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] not in trie:
                    continue
                dfs(i, j, trie)
        
        return matched_words
            
        
                
                    
            
        