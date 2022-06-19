class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = dict()
        KEY = '#'
        products.sort()
        def add(node, product):
            if product not in node:
                node = [product]
            else:
                node.append(product)
        for product in products:
            cur = trie
            for letter in product:
                cur = cur.setdefault(letter, {})
                if KEY in cur:
                    cur[KEY].append(product)
                else:
                    cur[KEY] = [product]
        newWord = ''
        cur = trie
        res = []
        flag = True
        for char in searchWord:
            if char not in cur or not flag:
                res.append([])
                flag = False
            elif flag:
                cur = cur[char]
                res.append(cur[KEY][:3])
        return res
                
        