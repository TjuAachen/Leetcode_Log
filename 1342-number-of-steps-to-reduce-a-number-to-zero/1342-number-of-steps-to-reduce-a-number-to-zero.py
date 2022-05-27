class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        pos = 0
        cur = 1
        if num == 0:
             return 0
        while(cur <= num):
            cur_num = num&cur
            if cur_num == 0:
                count += 1
            else:
                count += 2
            pos += 1
            cur = 1<<pos
        return count - 1
            