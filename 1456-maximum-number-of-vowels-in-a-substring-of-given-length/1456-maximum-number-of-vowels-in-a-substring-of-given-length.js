/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    var left = 0
    var right = 0
    var n = s.length
    var vowelNum = 0
    var vowels = "aeiou"
    var answer = 0
    
    while (right < n) {
        var cur = s[right]
        if (vowels.includes(cur))
            vowelNum += 1
        
        if (right - left == k - 1) {
            answer = Math.max(answer, vowelNum)
            var leftCur = s[left]
            if (vowels.includes(leftCur))
                vowelNum -= 1
            left += 1
        }
        right += 1
    }
    
    return answer
};