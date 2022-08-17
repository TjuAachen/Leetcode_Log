class Solution:
    def calculate(self, s: str) -> int:
        global i
        i = 0
        n = len(s)
        
        def calculate_res(s):
            global i
            num = 0
            oper = '+'
            stack = []
            
            while(i < n):
               # print(stack)
                cur = s[i]
                i += 1
                if '0' <= cur <= '9':
                    num = 10*num + int(cur)
                if cur == '(':
                    num = calculate_res(s)
                if cur == '+' or cur == '-' or cur == '*' or cur == '/' or cur == ')' or i == n:
                    if oper == '*':
                        stack.append(stack.pop() * num)
                    elif oper == '/':
                        popped = stack.pop()
                        division_res = abs(popped) // abs(num)
                        if popped * num < 0:
                            stack.append(-division_res)
                        else:
                            stack.append(division_res)
                    elif oper == '+':
                        stack.append(num)
                    elif oper == '-':
                        stack.append(-num)
                    oper = cur
                    num = 0
                if cur == ')':
                    break
           # print(stack)
            return sum(stack)
        return calculate_res(s)
                        
        