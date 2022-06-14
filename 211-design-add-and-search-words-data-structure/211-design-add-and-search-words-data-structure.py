from collections import deque
class node:
    def __init__(self, val = None):
        self.flag = False
        self.next = dict()
        self.val = val
class WordDictionary:

    def __init__(self):
        self.root = node()
        

    def addWord(self, word: str) -> None:
        i = 0
        word_len = len(word)
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
        queue = deque()
        queue.append(self.root)
        layer_num = 0
        word_len = len(word)
        while(queue and layer_num < word_len):
            size = len(queue)
            cur_char = word[layer_num]
            for i in range(size):
                popped = queue.popleft()
                for key, val in popped.next.items():
                    if key == cur_char or cur_char == '.':
                        queue.append(val)
                        if layer_num == word_len - 1 and val.flag:
                            return True
            layer_num += 1
        return False
                
               


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)