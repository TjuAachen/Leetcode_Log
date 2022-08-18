class Solution:
    def decodeString(self, s: str) -> str:
        global i
        i = 0
        n = len(s)
        def decode(s):
            global i
            num = 0
            char_set = []
          #  res = ''
            while(i < n):
                cur_char = s[i]
                i += 1
                if '0' <= cur_char <= '9':
                    num = num*10 + int(cur_char)
                elif cur_char == '[':
                    char_set.append(num*decode(s))
                    num = 0
                elif cur_char != ']':
                    char_set.append(cur_char)
                else:
                    break
                
            return ''.join(char_set) 
        return decode(s)