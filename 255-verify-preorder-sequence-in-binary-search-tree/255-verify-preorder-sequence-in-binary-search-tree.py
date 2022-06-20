class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        #low is the popped leftmost
        low = -float('inf')
        j = - 1
        for ind, elem in enumerate(preorder):
            if elem < low:
                return False
            while(j > - 1 and preorder[j] < elem):
                low = preorder[j]
                j = j - 1
            j += 1
            preorder[j] = elem
        return True
                
        
        
        
            
            