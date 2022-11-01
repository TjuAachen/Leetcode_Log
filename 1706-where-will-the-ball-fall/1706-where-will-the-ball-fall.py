class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        #simulation
        #to simulate, when a ball would be stuck? when it is not stuck?
        #by analysis, we can see when the pattern V is formed, i.e. 1 is in the left of -1. 1, -1
        #to simulate, we can traverse each element in the first row of the grid to represent each ball
        #for each ball, we can simulate its movement by adding deducting -1 from its indexes and in this process, we will exmaine whether it is stuck or not using the pattern above.
        #if it is stuck, then append -1. if it is not, append 1.
        #besides 1 -1 pattern, 1 can also form a V with the border, border -1 is also true.
        
        #1. traverse each entry in the first row
        #2. for each entry, we simulate the movement and examine whether it is stuck or not.
        #2.1 if true, then append -1
        #2.2 if not, then continue and append 1
        
        #3. to examine, we can check whether it is 1, -1/ 1, border/ border, -1 patterns
        
        res = []
        nrow, ncol = len(grid), len(grid[0])
        
        for col in range(ncol):
            isStuck = False
            for row in range(nrow):
                if self.isStuck(row, col, grid, ncol):
                    res.append(-1)
                    isStuck = True
                    break
                curVal = grid[row][col]
                col += curVal
            if not isStuck:
                res.append(col)
        return res
            
            
            
    def isStuck(self, row, col, grid, ncol):
        curVal = grid[row][col]
        if curVal == 1:
            if col == ncol - 1 or grid[row][col + 1] == -1:
                return True
        else:
            if col == 0 or grid[row][col - 1] == 1:
                return True
        return False
        
        
        
        