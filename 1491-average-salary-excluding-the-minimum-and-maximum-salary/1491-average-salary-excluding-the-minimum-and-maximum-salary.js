/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    var maxNum = salary.reduce((a, b) => Math.max(a, b), -Infinity);
    var minNum = salary.reduce((a, b) => Math.min(a, b), Infinity);
    var sumVal = salary.reduce((a, b) => {if (b != maxNum && b != minNum) {
        return a + b;
    }else {
        return a;
    }}, 0);
    var n = salary.reduce((a, b) => {if (b != maxNum && b != minNum) {
        return a + 1;
    }else {
        return a;
    }}, 0);
    
    return sumVal / n
};