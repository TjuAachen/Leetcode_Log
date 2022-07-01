
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if int(num) < target:
            return []
        N = len(num)
        res = []
        
        def recurse(index, pre_operand, cur_operand, value, string):
            if index == N:
                if target == value and cur_operand == 0:
                    res.append(''.join(string[1:]))
                return
            #
            cur_operand = 10*cur_operand + int(num[index])
            str_ops = str(cur_operand)
            #avoid 05, No operations
            if cur_operand > 0:
                recurse(index + 1, pre_operand, cur_operand, value,string)
            
            #set the end for the current operand and implement the operation
            #addition
            string.append('+')
            string.append(str_ops)
            recurse(index + 1, cur_operand, 0, value + cur_operand, string)
            string.pop()
            string.pop()
            if string:
                #subtraction
                string.append('-')
                string.append(str_ops)
                recurse(index + 1, -cur_operand, 0, value - cur_operand, string)
                string.pop()
                string.pop()     
                
                #multiplication
                string.append('*')
                string.append(str_ops)
                recurse(index + 1, cur_operand*pre_operand, 0, value - pre_operand + pre_operand*cur_operand, string)
                string.pop()
                string.pop()   
        recurse(0,0,0,0,[])
        return res
    

                    
        
        
        
        
                    
            
        
        