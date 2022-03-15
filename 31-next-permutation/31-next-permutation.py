class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        record = []
        for i in range(len(nums)-1,-1,-1):
            for j in range(i,-1,-1):
                if nums[i] > nums[j]:
                    if not record:
                        record = [i,j]
                    else:
                        if record[1] < j:
                            record = [i,j]
                    break
        if record:
            nums[record[0]],nums[record[1]] = nums[record[1]],nums[record[0]]
            nums[record[1]+1:] = sorted(nums[record[1]+1:])
        else:
            nums.sort()
        
        
        