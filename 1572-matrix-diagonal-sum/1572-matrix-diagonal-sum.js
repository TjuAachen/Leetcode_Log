/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    var nrow = mat.length
    var ncol = mat[0].length
    var res = 0
    
    for (var row = 0; row < nrow; row++) {
        var col = row
        var negCol = ncol - 1 - row
        if (col != negCol)
            res += mat[row][col] + mat[row][negCol]
        else{
            res += mat[row][col]
        }
    }
    
    return res
};