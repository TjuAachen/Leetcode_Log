class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def examine(string,flag):
        #flag = 0, ipv4:
            if flag == 0:
                if len(string) > 3 or len(string) == 0:
                    return False
                if len(string)>1 and string[0] == '0':
                    return False
                if string.isnumeric() and 0 <= int(string) <= 255:
                    return True
                else:
                    return False
        #flag = 1, ipv6
            if flag == 1:
                if 1 <= len(string) <= 4:
                    for i in string:
                        if i.lower() > 'f':
                            return False
                    return True
                else:
                    return False
        string = ''
        flag_array = []
        for i in queryIP:
            if i != '.' and i != ':':
                string = string + i
            if i == '.':
                if len(flag_array) > 0 and 1 in flag_array:
                    return 'Neither'
                flag_array.append(0)
                if examine(string, 0) == False:
                    return 'Neither'
                string = ''
            elif i == ':':
                if len(flag_array) > 0 and 0 in flag_array:
                    return 'Neither'
                flag_array.append(1)
                if examine(string, 1) == False:
                    return 'Neither'
                string = ''
        if len(flag_array) == 3 and flag_array[0] == 0:
            if examine(string, 0):
                return 'IPv4'
        if len(flag_array) == 7 and flag_array[0] == 1:
            if examine(string, 1):
                return 'IPv6'
        return 'Neither'
