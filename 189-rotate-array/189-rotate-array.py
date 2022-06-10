class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        k_refined = k % length
        
        while(k_refined > 0):
            popped = nums.pop()
            nums.insert(0, popped)
            k_refined = k_refined - 1
        