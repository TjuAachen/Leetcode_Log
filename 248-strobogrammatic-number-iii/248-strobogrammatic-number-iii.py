class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        nxt = [('', ''),('0','0'),('1','1'),('8','8'),('9','6'),('6','9')]
        center = [('',''),('0','0'),('1','1'),('8','8')]
        
        global count
        count = 0
        temp = []
        counted = set()
        max_step = len(high) // 2
        int_high, int_low = int(high), int(low)
        def dfs(step):
            global count
            if step == max_step:
                cur = ''.join(temp)
                if cur == '':
                    int_cur = -1
                else:
                    int_cur = int(cur)
                leading_zero = False
                if cur and cur[0] == '0' and len(cur) != 1:
                    leading_zero = True
                if not leading_zero and int_cur not in counted and int_cur <= int_high and int_cur >= int_low:
                    count += 1
                    counted.add(int_cur)
                return
            # even number
            for left, right in nxt:
                if step == max_step - 1 and left == '0':
                    continue
                temp.append(right)
                temp.insert(0,left)
                dfs(step + 1)
                temp[:] = temp[1:-1]
        for left, right in center:
            temp.append(left)
            dfs(0)
            temp.pop()
        return count