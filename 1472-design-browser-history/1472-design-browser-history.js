/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.history = []
    this.history.push(homepage)
    this.idx = 0
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    this.history = this.history.slice(0, this.idx + 1)
    this.idx += 1
    this.history.push(url)
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    this.idx = Math.max(0, this.idx - steps)
    if (this.history.length > 0)
        return this.history[this.idx]
    
    return null
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    this.idx = Math.min(this.idx + steps, this.history.length - 1)
    
    if (this.idx >= 0)
        return this.history[this.idx]
    return null
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */