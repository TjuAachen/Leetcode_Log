class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)
        digits = len(nums)
        stack = []
        inc = 2**31-1
        ans = []
        int_32 = str(inc)
        if digits > len(str(2**31-1)):
                return -1
        def helper(s, ans):
            s = list(s)
            if not ans:
                return -1
            s[ans[0]], s[ans[1]] = s[ans[1]], s[ans[0]]
            s = s[:ans[0]+1] + sorted(s[ans[0]+1:])
            if int("".join(s)) > int(int_32):
                return -1
            return int("".join(s))
            
            
        for ind in range(digits-1,-1,-1):
            i = nums[ind]
            num_i = int(i)
            if not stack:
                stack.append([ind,num_i])
            elif stack[-1][1] <= num_i:
                stack.append([ind,num_i])
            else:
                while(stack and stack[-1][1]>num_i):
                    popped = stack.pop()
                    inc_temp = (popped[1] - num_i)*(10**(digits-1-ind)-10**(digits-1-popped[0]))
                    if inc_temp < inc:
                        ans = [ind,popped[0]]
                        inc = inc_temp
        return helper(nums, ans)
        
        
                        
                    
            