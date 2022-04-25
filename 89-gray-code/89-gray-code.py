class Solution:
    def grayCode(self, n: int) -> List[int]:
        def generate(n):
            if n == 1:
                return [0,1]
            prev = generate(n-1)
            temp = []
            for i in range(len(prev)-1,-1,-1):
                temp.append(prev[i] + 2**(n-1))
            return prev + temp
        
        return generate(n)       
        
            
        
            