class node:
    def __init__(self, val = None):
        self.flag = False
        self.next = dict()
        self.val = val
class Trie:
    def __init__(self):
        self.root = node()

    def insert(self, word: str) -> None:
        word_len = len(word)
        i = 0
        cur_node = self.root
        while(i < word_len):
            cur_char = word[i]
            if cur_char not in cur_node.next:
                next_node = node(cur_char)
                cur_node.next[cur_char] = next_node
            else:
                next_node = cur_node.next[cur_char]
            if i == word_len - 1:
                next_node.flag = True
            cur_node = next_node
            i = i + 1
        
                
            
        
        

    def search(self, word: str) -> bool:
        word_len = len(word)
        i = 0
        cur_node = self.root
        while(i < word_len):
            cur_char = word[i]
            if cur_char not in cur_node.next:
                return False
            else:
                next_node = cur_node.next[cur_char]
            cur_node = next_node
            i = i + 1 
        if cur_node.flag:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        word_len = len(prefix)
        i = 0
        cur_node = self.root
        while(i < word_len):
            cur_char = prefix[i]
            if cur_char not in cur_node.next:
                return False
            else:
                next_node = cur_node.next[cur_char]
            cur_node = next_node
            i = i + 1   
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)