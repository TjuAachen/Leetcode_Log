class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        #convert the expression into two stacks
        i = 0
        expre_len = len(expression)
        num, oper = [], []
        #symbol : *: 0, +: 1, -: -1
        while(i < expre_len):
            cur = expression[i]
            if cur == '*':
                oper.append(0)
            elif cur == '-':
                oper.append(-1)
            elif cur == '+':
                oper.append(1)
            elif '0' <= cur <= '9':
                if i < expre_len - 1 and '0' <= expression[i+1] <='9':
                    num.append(int(cur+expression[i+1]))
                    i = i + 1
                else:
                    num.append(int(cur))
            i = i + 1
        #edge case
        if not oper:
            return num
        global res, combination
        res = []
        combination_set = set()
        index = [(i,i) for i in range(len(num))]
        record = [0] * len(num)

        
        def calculate(num, oper, index):
            global res
            if len(oper) == 0:
                key = tuple(record[:])
                if key not in combination_set:
                    res.extend(num[:])
                    combination_set.add(key)
                return 
            for i,sym in enumerate(oper):
                num1, num2 = num[i], num[i+1]
                val = (1-abs(sym)) * (num1*num2)+ (num1 + sym*num2)*abs(sym)
                temp = num[i+1]
                num[i+1] = val
                #update
                temp_num = num[:i] + num[i+1:]
                temp_oper = oper[:i] + oper[i+1:]
                left, right = index[i][0], index[i+1][-1]
                
                temp_order = index[:i] + index[i+1:]
                temp_order[i] = (left, right)
                record[left] += 1
                record[right] = record[right] - 1
                
                calculate(temp_num[:], temp_oper[:], temp_order)
                num[i+1] = temp
                record[left] = record[left] - 1
                record[right] += 1
        calculate(num[:], oper[:], index)
        return res
        
                