/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    var nrow = grid.length
    var ncol = grid[0].length;
    
    for (var i = 1; i < nrow; i++) grid[i][0] += grid[i - 1][0]
    for (var j = 1; j < ncol; j++) grid[0][j] += grid[0][j - 1]
    
    for (var i = 1; i < nrow; i++) 
        for (var j = 1; j < ncol; j++) {
            grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1])
        }
    
    return grid[nrow - 1][ncol - 1]
};