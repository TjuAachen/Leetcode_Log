/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    var res = []
    var n1 = word1.length
    var n2 = word2.length
    var n = Math.max(n1, n2)
    
    for (var i = 0; i < n; i++) {
        if (i < n1)
            res.push(word1[i])
        if (i < n2)
            res.push(word2[i])
    }
    
    return res.join("")
    
    
    
};