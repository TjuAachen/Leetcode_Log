class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_to_index = defaultdict(int)
        
        count = 0
        is_exist_same = False
        for i, word in enumerate(words):
            word_to_index[word] += 1
        for key, val in word_to_index.items():
            reversed_key = key[::-1]
            if reversed_key == key:
                count += val//2 * 4
                word_to_index[key] = val - val//2 * 2
                if word_to_index[key] > 0:
                    is_exist_same = True
            elif reversed_key in word_to_index:
                cur_val = min(word_to_index[reversed_key], val)
                count += cur_val * 4
                word_to_index[key] -= cur_val
                word_to_index[reversed_key] -= cur_val
        if is_exist_same:
            count += 2
        return count