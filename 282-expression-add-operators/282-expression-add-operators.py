
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if int(num) < target:
            return []
        cur_val = []
        global cal_res, pre_sym, pre_val, cur_val
        cal_res = 0
        num = num[::-1]
        n = len(num)
        #1:*, None:others
        pre_sym = -1
        pre_val = -1
        
        #collections of final results
        res = []
        temp = []
        
        def dfs(start):
            global cal_res, pre_val, pre_sym, cur_val
            if start == n:
                if cal_res == target:
                    cur = temp[::-1]
                    res.append(''.join(cur))
                return
            if start == n - 1:
                temp_cur_val = cur_val[:]
                if pre_sym == 1:
                    cur_val.insert(0, num[start])
                    temp_res = pre_val*int(''.join(cur_val))
                else:
                    cur_val.insert(0, num[start])
                    temp_res = int(''.join(cur_val))
                if len(cur_val)>1 and int(cur_val[0]) == 0:
                    cur_val = temp_cur_val[:]
                    return
                temp.append(num[start])
                cal_res += temp_res
                dfs(start + 1)
                cur_val = temp_cur_val[:]
                temp.pop()
                cal_res -= temp_res
                return
            for oper in ['*','-','+','']:
                if num[start] == '0' and oper != '' and cur_val:
                    continue
                temp_pre_val = pre_val
                temp_pre_sym = pre_sym
                temp_cur_val = cur_val[:]
                cur_val.insert(0, num[start])
                temp_res = 0
                
                temp.append(num[start])
                temp.append(oper)
            
            
                if oper == '*':
                    if pre_val != -1:
                        pre_val = int(''.join(cur_val[:])) * pre_val
                    else:
                        pre_val = int(''.join(cur_val[:]))
                    cur_val = []
                    pre_sym = 1
                elif oper == '+':
                    if pre_val != -1:
                        temp_res = int(''.join(cur_val[:])) * pre_val
                    else:
                        temp_res = int(''.join(cur_val[:])) 
                    cal_res += temp_res
                    cur_val = []
                    pre_sym = -1
                    pre_val = -1
                elif oper == '-':
                    if pre_val != -1:
                        temp_res = int(''.join(cur_val[:])) * pre_val
                    else:
                        temp_res = int(''.join(cur_val[:])) 
                    cal_res -= temp_res 
                    cur_val = []
                    pre_sym = -1
                    pre_val = -1
                dfs(start + 1)
                pre_sym = temp_pre_sym
                pre_val = temp_pre_val
                if oper == '+':
                    cal_res -= temp_res
                elif oper == '-':
                    cal_res += temp_res
                cur_val = temp_cur_val[:]
                temp.pop()
                temp.pop()
        dfs(0)
        return res

                    
        
        
        
        
                    
            
        
        