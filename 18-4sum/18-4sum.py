class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        final = []
        i = 0
        while(i < n - 3):
            first = nums[i]
            j = i + 1
            while(j < n - 2):
                second = nums[j]
                left, right = j+1, n - 1
                while(left < right):
                    third, fourth = nums[left], nums[right]
                    total = first + second + third + fourth
                    if total == target:
                        final.append([first, second, third, fourth])
                        while(left < right and third == nums[left]):
                            left = left + 1
                        while(left < right and fourth == nums[right]):
                            right = right - 1
                    elif total < target:
                        left = left + 1
                    else:
                        right = right - 1
                while(j < n - 2 and second == nums[j]):
                    j = j + 1
                
            while( i < n - 3 and nums[i] == first):
                i = i + 1
        return final
                    
        