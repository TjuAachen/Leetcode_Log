/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
function search(matrix, row, col, res) {
    var nrow = matrix.length
    var ncol = matrix[0].length
    
    if (row < 0 || row >= nrow || col < 0 || col >= ncol || matrix[row][col] == -101)
        return
    res.push(matrix[row][col])
    matrix[row][col] = -101
    //right
    if (col + 1 >= row)
        arguments.callee(matrix, row, col + 1, res)
    //down
    arguments.callee(matrix, row + 1, col, res)
    //left
    arguments.callee(matrix, row, col - 1, res)
    //up
    arguments.callee(matrix, row - 1, col, res)
}

var spiralOrder = function(matrix) {
    //use recursion
    var res = []
    search(matrix, 0, 0, res)
    
    return res
    
};