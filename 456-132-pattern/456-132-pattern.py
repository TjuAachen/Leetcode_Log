class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        k = None
        for num in reversed(nums):
            #print(num, k)
            if k != None and num < k:
                    return True
            if not stack or stack[-1] > num:
                stack.append(num)
            else:
                while(stack and stack[-1] <= num):
                    popped = stack.pop()
                    #print(popped, num, k)
                    if k == None and popped != num:
                        k = popped
                    elif popped != num:
                        k = max(popped, k)
                stack.append(num)
                #print(k)
            #print(k)
        return False
            
        