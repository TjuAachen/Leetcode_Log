/**
 * @param {number[][]} grid
 * @return {number}
 */
function bfs(row, col, grid) {
    var queue = [[row, col]]
    var nrow = grid.length
    var ncol = grid[0].length
    
    nxtSteps = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    
    grid[row][col] = 0
    while (queue.length > 0) {
     //   console.log(queue)
        var [curRow, curCol] = queue.shift()
    for (var [dx, dy] of nxtSteps) {
        var nxtRow = curRow + dx
        var nxtCol = curCol + dy
        if (nxtRow < 0 || nxtRow >= nrow || nxtCol < 0 || nxtCol >= ncol)
            continue
        if (grid[nxtRow][nxtCol] == 0)
            continue
        grid[nxtRow][nxtCol] = 0
        queue.push([nxtRow, nxtCol])
    }
    }
    
}

var numEnclaves = function(grid) {
    // exclusion principle
    var nrow = grid.length
    var ncol = grid[0].length
    
    //go through the first/last row
    for (var col = 0; col < ncol; col++) {
        if (grid[0][col] == 1) {
            bfs(0, col, grid)
        }
        if (grid[nrow - 1][col] == 1){  
            bfs(nrow - 1, col, grid)
        }
    }
    
        //go through the first/last col
    for (var row = 0; row < nrow; row++) {
        if (grid[row][0] == 1) {
            bfs(row, 0, grid)
        }
        if (grid[row][ncol - 1] == 1){
           // console.log(row, ncol - 1)
            bfs(row, ncol - 1, grid)
        }
    }

    var ans = 0
    for (var row = 0; row < nrow; row++)
        for (var col = 0; col < ncol; col++) {
            if (grid[row][col] == 1)
                ans++
        }
    
    return ans
};