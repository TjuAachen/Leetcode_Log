from bisect import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)

        bucket = dict()
        
        def hashFunc(num):
            return num//(t+1)
            
        left, right = 0, 0
        while(right < n):
            index = hashFunc(nums[right])
            if index in bucket:
                return True
            if index - 1 in bucket and abs(bucket[index - 1] - nums[right]) <= t:
                return True
            if index + 1 in bucket and abs(bucket[index + 1] - nums[right]) <= t:
                return True
            bucket[index] = nums[right]
            right = right + 1
            if right - left == k + 1:
                index = hashFunc(nums[left])
                bucket.pop(index)
                left = left + 1
        return False
            
        
        