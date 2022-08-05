class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        x_axis = -b*float('inf')
        if a != 0:
            x_axis = - b / (2*a)
        
        nums_left = []
        nums_right = []
        
        def quadratic(x):
            return a * x**2 + b * x + c
        
        for num in nums:
            transformed_val = quadratic(num)
            if num <= x_axis:
                nums_left.append(transformed_val)
            else:
                nums_right.append(transformed_val)
            
        
        
        if a >= 0:
            nums_left, nums_right = nums_right, nums_left
        
        left_count, right_count = len(nums_left), len(nums_right)
        p, q = 0, right_count - 1
        res = []
        while(p < left_count or q >= 0):
            left, right = float('inf'), float('inf')
            if p < left_count:
                left = nums_left[p]
            if q >= 0:
                right = nums_right[q]
            if left == min(left, right):
                p += 1
                res.append(left)
            else:
                q -= 1
                res.append(right)
        return res
            
            
                
        