class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        n = len(data)
        def is_valid(i, num):
            if i >= n - num:
                return False
            for j in range(i+1, i + num + 1):
                cur_num = data[j]
                if not cur_num&(1<<7) or cur_num&(1<<6):
                    return False
            return True
        while(i < n):
            cur_num = data[i]
            bit_one, bit_two, bit_three, bit_four, bit_five = cur_num&(1<<7), cur_num&(1<<6), cur_num&(1<<5), cur_num&(1<<4), cur_num&(1<<3)
            if bit_one == 0:
                i += 1
                continue
            if bit_two == 0:
                return False
            if bit_three == 0:
                if is_valid(i, 1):
                    i = i + 2
                    continue
                return False
            if bit_four == 0:
                if is_valid(i, 2):
                    i = i + 3
                    continue
                return False
            if bit_five == 0:
                if is_valid(i, 3):
                    i = i + 4
                    continue
                return False   
            else:
                return False
        return True
                
        