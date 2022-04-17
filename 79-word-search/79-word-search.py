class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        length = len(word)
        visited = dict()
        record = dict()
        def find(i,j, k):
            if (i,j,k) in record:
                return record[(i,j,k)]
            dire = [(0,1),(0,-1),(1,0),(-1,0)]
            if k == length:
                return True
            if word[k] != board[i][j]:
                return False
            for nxt in dire:
                newX, newY = i+nxt[0], j + nxt[1]
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                    visited[(newX,newY)] = 1
                    if find(newX, newY, k+1):
                        record[(newX,newY,k+1)] = True
                        record[(i,j,k)] = True
                        return record[(newX,newY,k+1)]
                    del visited[(newX,newY)]
            if k+1 == length:
                record[(i,j,k)] = True
                return True
      #      else:
            
      #          record[(i,j,k)] = False        
            return False
        for i in range(m):
            for j in range(n):
                visited[(i,j)] = 1
                if find(i,j, 0):
                    return True
                del visited[(i,j)]
        return False
                        
                    
            
        