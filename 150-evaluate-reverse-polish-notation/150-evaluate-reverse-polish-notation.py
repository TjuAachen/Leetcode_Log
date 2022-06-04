class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set(['+','-','*','/'])
        stack = []
        length = len(tokens)
        #find the bottom
        cur = 0
        def calculate(num1, num2, sym):
            if sym == '+':
                return int(num1) + int(num2)
            if sym == '-':
                return int(num1) - int(num2)
            if sym == '*':
                return int(num1) * int(num2)
            if sym == '/':
                return int(int(num1) / int(num2))
        while(cur < length):
            token = tokens[cur]
            if token in operator and len(stack) > 1:
                if stack[- 1] not in operator and stack[-2] not in operator:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(calculate(num1, num2, token))
            else:
                stack.append(int(token))
            cur += 1
        return stack.pop()
        
                    
            
                
                