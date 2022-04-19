class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        symbol = []
        num = []
        i = 0
        sym = 0
        cur = 0
        while(i < n):
            char = s[i]
            if char == "*":
                sym = 3
                i = i + 1
            elif char == "/":
                sym = 4
                i = i + 1
            elif char == "+":
                sym = 1
                i = i + 1
            elif char == "-":
                sym = 2
                i = i + 1
            elif ("0" <= char <= "9"):
                number = 0
                while(i < n and "0" <= s[i] <= "9"):
                    number = number*10+int(s[i])
                    i = i + 1
                
                if sym == 3:
                    num.append(num.pop() * number)
                elif sym == 4:
                    num.append(num.pop() // number)
                elif sym in [1,2]:
                    if symbol:
                        l1 = num.pop()
                        l2 = num.pop()
                        oper = symbol.pop()
                        if oper == 2:
                            num.append(l2-l1)
                        else:
                            num.append(l1+l2)
                        symbol.append(sym)
                      #  num.append(cur)
                        num.append(number)
                    else:
                        symbol.append(sym)
                        num.append(number)
                else:
                    num.append(number)
            else:
                i = i + 1
      #      print(num,symbol)
        if symbol:
            l1 = num.pop()
            l2 = num.pop()
            oper = symbol.pop()
            if oper == 2:
                cur = l2 - l1
            else:
                cur = l1+l2      
        elif num:
            cur = num[-1]
        return cur
                
                            
        