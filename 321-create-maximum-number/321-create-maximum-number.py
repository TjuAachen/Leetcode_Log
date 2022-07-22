class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def createMax(nums, k):
            n = len(nums)
            remaining = n - k
            
            stack = []
            for char in nums:
                while(remaining and stack and stack[-1] < char):
                    remaining -= 1
                    stack.pop()
                stack.append(char)
            if remaining > 0:
                return stack[:-remaining]
            return stack
        
        def merge(max1, max2):
            p1, p2 = 0, 0
            len1, len2 = len(max1), len(max2)
            res = []
            while(max1 or max2):
                if max1 > max2:
                    bigger = max1
                else:
                    bigger = max2
                res.append(bigger[0])
                bigger.pop(0)
            return res
        
        n1, n2 = len(nums1), len(nums2)
        res = None
        for i in range(k+1):
            k1, k2 = i, k - i
            if k1 <= n1 and k2 <= n2:
                max1, max2 = createMax(nums1, k1), createMax(nums2, k2)
                if not res:
                    res = merge(max1, max2)
                else:
                    res = max(res, merge(max1,max2))
        return res
                
                
                    
        
        