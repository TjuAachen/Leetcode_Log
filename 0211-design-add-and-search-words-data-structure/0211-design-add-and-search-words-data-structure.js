
var WordDictionary = function() {
    this.map = new Map()
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    var map = this.map;
    
    for (var i = 0; i < word.length; i++) {
        var curChar = word.charAt(i)
        if (!map.has(curChar)) {
            map.set(curChar, new Map())
        }
        map = map.get(curChar)
    }
    
    map.set('*', new Map())

};

/** 
 * @param {string} word
 * @return {boolean}
 */

function searchInTrie(word, start, trie) {
    if (start == word.length && trie.has('*'))
        return true
    
    var curChar = word.charAt(start);
    
    if (curChar == '.') {
        for (const key of trie.keys()) {
            var curRes = arguments.callee(word, start + 1, trie.get(key))           
            if (curRes == true)
                return true    
        }
    }
    if (trie.has(curChar)) {
        return arguments.callee(word, start + 1, trie.get(curChar))
    }
    
    return false
    
    
    
    
    
};

WordDictionary.prototype.search = function(word) {

    return searchInTrie(word, 0, this.map)
    
};
    

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */