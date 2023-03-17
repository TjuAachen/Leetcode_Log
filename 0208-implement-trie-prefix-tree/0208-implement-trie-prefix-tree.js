
var Trie = function() {
    this.map = new Map()
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    var map = this.map;
    
    for (let i = 0; i < word.length; i++) {
        var curChar = word.charAt(i)
        if (!map.has(curChar))
            map.set(curChar, new Map())
        map = map.get(curChar)
    }
    map.set('*', new Map())

};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    var map = this.map;
    
    for (let i = 0; i < word.length; i++) {
        var curChar = word.charAt(i)
        if (!map.has(curChar))
            return false
        map = map.get(curChar)
    }
    if (map.get('*'))
        return true
    return false
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    var map = this.map;
    
    for (let i = 0; i < prefix.length; i++) {
        var curChar = prefix.charAt(i)
        if (!map.has(curChar))
            return false
        map = map.get(curChar)
    }
    return true
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */