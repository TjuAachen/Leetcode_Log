class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        end = len(nums)
        right = 0
        left = 0
        record = dict()
        
        while(right < end):
            if nums[right] in record:
                return True
            record[nums[right]] = 1
            right = right + 1
            if right - left == k + 1:
                record.pop(nums[left])
                left = left + 1
        return False
                
            
            