class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_integer(s,ind,right):
            if s == '' or not s:
                return True
            if ind == 1 and len(s) == 1 and s[0] in ['+','-']:
                return False
            if ind == 0 and len(s) == 1 and s[0] in ['+','-'] and (not right or (right[0] in ['+','-'] and len(right) == 1)):
                return False
            if not ('0' <= s[0] <= '9') and not s[0] in ['+','-']:
                return False
            i = 0
            if s[0] in ['+','-']:
                i = 1
            n = len(s)
            while(i < n):
                if not ('0' <= s[i] <= '9'):
                    return False
                i += 1
            return True
        def is_decimal(s):
            if s == '' or not s:
                return True
            if not ('0' <= s[0] <= '9') and s[0] not in ['+','-'] and s[0] != '.':
                return False
            i = 0
            n = len(s)
            integer = []
            integer1 = []
            flag = True
            while(i < n):
                if s[i] == '.' and flag:
                    flag = False
                    integer1[:] = integer[:]
                    integer = []
                elif s[i] == '.' and not flag:
                    return False
                elif i > 0 and not ('0' <= s[i] <= '9'):
                    return False
                else:
                    integer.append(s[i])
                i = i + 1
            if not integer and not integer1:
                return False
            elif not flag and not is_integer(integer1,0,integer):
                return False
            elif not flag and is_integer(integer,1,[]) and is_integer(integer1,0,integer):
                return True
            elif flag and is_integer(integer,0,[]):
                return True
            return False
        def is_valid(s):
            if s == '' or not s:
                return False
            if not ('0' <= s[0] <= '9') and s[0] not in ['+','-'] and s[0] != '.':
                return False
            decimal, decimal1 = [], []
            i = 0
            n = len(s)
            flag = True
            while(i < n):
                if s[i] in ['e','E'] and flag:
                    flag = False
                    decimal1[:] = decimal[:]
                    decimal = []
                    j = i
                elif s[i] in ['e','E'] and not flag:
                    return False
                elif i > 0 and not flag and i != (j+1) and not ('0' <= s[i] <= '9'):
                    return False
                else:
                    decimal.append(s[i])
                i = i + 1
            if (not decimal or not decimal1) and not flag:
                return False
            elif not flag and is_integer(decimal,1,[]) and is_decimal(decimal1):
                return True
            elif flag and is_decimal(decimal):
                return True
            else:
                return False
        return is_valid(s)
                    
                          
                    
                    