class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target < nums[0] and target > nums[-1]:
            return False
        num_rem = []
        for num in nums:
            if not num_rem or num_rem[-1] != num:
                num_rem.append(num)
        n = len(num_rem)
        if num_rem[-1] == num_rem[0] and n!=1:
            num_rem.pop()
        left, right = 0, len(num_rem) - 1
        while(left <= right):
            mid = left + (right - left)//2
            if num_rem[mid] == target:
                return True
            elif num_rem[mid] < target:
                if target >= num_rem[0] and num_rem[mid] <= num_rem[-1] and num_rem[0] > num_rem[-1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if num_rem[mid] >= num_rem[0] and target <= num_rem[-1] and num_rem[0] > num_rem[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        