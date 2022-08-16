class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []        
        i = 0
        n = len(input)
        res = 0
        def count_name_len(file_name_len, i, is_dir):
            while(i < n and input[i] != '\n'):
                  #  print(i, n, input[i])
                file_name_len += 1
                if input[i] == '.':
                    is_dir = False
                i = i + 1
            return file_name_len, i, is_dir
        while(i < n):
           # print(stack, i)
            cur = input[i]
            if cur == '\n' :
                i = i + 1
                num_t = 0
                while(i < n and input[i] == '\t'):
                    i = i + 1
                    num_t += 1
                #find the prev dire
                while(stack and stack[-1][0] >= num_t):
                    stack.pop()
                #count the length of file name or dir name
                file_name_len = 0
                is_dir = True
                file_name_len, i, is_dir = count_name_len(file_name_len, i, is_dir)
                if is_dir:
                    if stack:
                        stack.append([num_t, stack[-1][1] + file_name_len + 1])
                    else:
                        stack.append([num_t, file_name_len + 1])
                        
                else:
                    if stack:
                        res = max(res, file_name_len + stack[-1][1])
                    else:
                        res = max(res, file_name_len)
                      
            else:
                file_name_len = 0
                is_dir = True
                file_name_len, i, is_dir = count_name_len(file_name_len, i, is_dir)
                if is_dir:
                    stack.append([0, file_name_len+1])
                else:
                    res = file_name_len
                #print(i)
        return res
        
                
        