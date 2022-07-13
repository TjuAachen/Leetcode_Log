class Solution(object):
    def is_additive(self, num, prev_two, prev_one):
        global memoir
        n = len(num)  

        key = (num, prev_two, prev_one)
        
        if key in memoir:
            return memoir[key]
        
        cur_num = 0
        
        for i in range(n):
            #no leading zero
            if i > 0 and cur_num == 0:
                continue
            cur_num = 10*cur_num + int(num[i])
            if prev_one == None or prev_two == None:
                temp = self.is_additive(num[i+1:],prev_one, cur_num)
                if temp:
                    memoir[key] = True
                    return True
            elif prev_one + prev_two == cur_num:
                if i + 1 == n:
                    memoir[key] = True
                    return True
                temp = self.is_additive(num[i+1:],prev_one, cur_num)
                if temp:
                    memoir[key] = True
                    return True
            
            elif prev_one + prev_two < cur_num:
                memoir[key] = False
                return False
        memoir[key] = False
        return False            
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        global memoir
        memoir = {}
        return self.is_additive(num, None, None)
        