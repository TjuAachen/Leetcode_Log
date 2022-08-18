class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        
        required_num = len(arr) // 2
        
        sorted_freq_list = sorted(freq.values(), reverse = True)
        
        count = 0
        removed_num = 0
        #print(sorted_freq_list)
        for freq_val in sorted_freq_list:
            count += 1
            removed_num += freq_val
            if removed_num >= required_num:
                return count
        