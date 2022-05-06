class Solution:
    
    #question to clarity
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        i = 0
        cur = -1
        #i is current position
        while(i < len(s)):
            stack.append(s[i])
            i += 1
            cur += 1
            while cur >= k - 1 and stack[cur] == stack[cur-k+1]:
                is_delete = True
                for j in range(cur-k+1,cur+1):
                    if stack[j] != stack[cur-k+1]:
                        is_delete = False
                        break
                if is_delete:
                    stack = stack[:(cur-k+1)]
                    cur = cur - k
                else:
                    break
        return ''.join(stack)
                
            
        