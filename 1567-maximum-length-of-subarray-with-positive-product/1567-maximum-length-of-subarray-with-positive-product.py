class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start = 0
        neg_pos = []
        max_length = 0
        for i, elem in enumerate(nums):
            if elem < 0:
                neg_pos.append(i)  
            if elem == 0 or i == len(nums) - 1:
                if len(neg_pos)%2 == 0:
                    if nums[start] != 0 and elem != 0:
                        max_length = max(max_length,i-start + 1)
                    elif nums[start] == 0 and elem == 0:
                        max_length = max(max_length,i-start-1)
                    else:
                        max_length = max(max_length,i-start)
                else:
                    left = neg_pos[-1] - start
                    if elem <= 0:
                        right = i - neg_pos[0] - 1
                    else:
                        right = i - neg_pos[0] 
                    max_length = max(max_length,max(left,right))
                start = i + 1
                neg_pos = []
             
        return max_length
            
        