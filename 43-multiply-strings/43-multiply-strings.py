class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        first_num, second_num = num1[::-1], num2[::-1]
        stack = [0] * (l1+l2)
        for place1, digit1 in enumerate(first_num):
            for place2, digit2 in enumerate(second_num):
                num_zero = place1 + place2
                temp = int(digit1)*int(digit2) + stack[num_zero] 
                stack[num_zero] = temp%10
                stack[num_zero+1] += temp//10
        while len(stack) > 1 and stack[-1] == 0:
            stack.pop()
        return ''.join(str(num) for num in reversed(stack))
                
                