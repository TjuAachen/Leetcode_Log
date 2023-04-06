/**
 * @param {number[][]} grid
 * @return {number}
 */

function bfs(grid, row, col) {
    const queue = []
    queue.push([row, col])
    var nrow = grid.length
    var ncol = grid[0].length
    var nxtSteps = [[1,0], [0, 1], [-1, 0], [0, -1]]

    grid[row][col] = 1
    var isPossible = true
    if (row == nrow - 1 || row == 0 || col == 0 || col == ncol - 1) {

        isPossible = false
    }
  //  var isPossible = true
    
    while (queue.length > 0) {
        [curRow, curCol] = queue.shift()
        
        for (nxt of nxtSteps) {
            [rowStep, colStep] = nxt
            newRow = rowStep + curRow
            newCol = colStep + curCol
            
            if (newRow >= nrow || newRow < 0 || newCol >= ncol || newCol < 0)
                continue
            if (grid[newRow][newCol] == 1)
                continue
            if(newRow == nrow - 1 || newRow == 0 || newCol == ncol - 1 || newCol == 0){
                isPossible = false
            }
            grid[newRow][newCol] = 1
            queue.push([newRow, newCol])
        }
    }
    
    return isPossible
    
}

var closedIsland = function(grid) {

    var nrow = grid.length
    var ncol = grid[0].length
    var res = 0
    
    for (var row = 0; row < nrow; row++)
        for (var col = 0; col < ncol; col++) {
            if (grid[row][col] == 0 && bfs(grid, row, col)) {
                res += 1
            }
        }
   // console.log(grid)
    return res
};
