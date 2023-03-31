/**
 * @param {string[]} pizza
 * @param {number} k
 * @return {number}
 */
var memo = new Map()
var MOD = 1000000007



function isPossible(startRow, startCol, endRow, endCol, prefix, k) {


    var num = prefix[endRow + 1][endCol + 1] + prefix[startRow][startCol] - prefix[endRow + 1][startCol] - prefix[startRow][endCol + 1]
   // console.log(startRow, startCol, endRow, endCol, prefix, num, k)
    return num >= k
    
}

function count(startRow, startCol, endRow, endCol, prefix, k) {
    var key = startRow +"#"+startCol + "#"+ endRow.toString()+"#" + endCol +"#"+k
    var ans = 0
    if (memo.has(key))
        return memo.get(key)
    if (k == 1) {
        memo.set(key, 1)
        return 1
    }
    for (var row = startRow; row < endRow; row++) {
        if (isPossible(startRow, startCol, row, endCol, prefix, 1) && isPossible(row + 1, startCol, endRow, endCol, prefix, k - 1)) {
            ans = (ans + arguments.callee(row + 1, startCol, endRow, endCol, prefix, k - 1)) % MOD 
        }
    }
 
    for (var col = startCol; col < endCol; col++) {
        if (isPossible(startRow, startCol, endRow, col, prefix, 1) && isPossible(startRow, col + 1, endRow, endCol, prefix, k - 1)) {
            ans = (ans + arguments.callee(startRow, col + 1, endRow, endCol, prefix, k - 1)) % MOD 
        }
    }
    
    memo.set(key, ans)
    
    return ans
    
    
}


var ways = function(pizza, k) {
    memo = new Map()
    var nrow = pizza.length
    var ncol = pizza[0].length
    var zeros = [0]
    
    for (var col = 0; col < ncol; col++) {
        zeros.push(0)
    }
        
    var prefix = [zeros]
    
    for (var row = 0; row < nrow; row++){
        var curRow = [0]
        for (var col = 0; col < ncol; col++) {
            var curVal = 0
            if (pizza[row].charAt(col) == 'A') {
                curVal += 1
            }
            var left = 0
            var up = 0
            var middle = 0
            left = curRow[col]
            up = prefix[row][col + 1]
            middle = prefix[row][col]
          //  console.log(row, col, left, up, middle, curVal, prefix)
            curVal += left + up - middle
            
            
            curRow.push(curVal)
        }

        prefix.push(curRow)
    }

    return count(0, 0, nrow - 1, ncol - 1, prefix, k)
    
    
};