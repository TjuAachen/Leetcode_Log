class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #negative and 0 are specially treated
        length = len(nums)
        i = 0
        flag = False
        candidate = -float('inf')
        max_product = -float('inf')
        length_later = -1
        while(i < length):
            j = i
            ans = 1
            while(j < length and nums[j] != 0):
                ans = ans * nums[j]
                if candidate == -float('inf') and ans < 0:
                    candidate = ans
                    length_later = 0
                max_product = max(max_product, ans)
                if length_later >= 0:
                    length_later += 1
                j += 1
            if ans < 0 and length_later > 1:
                max_product = max(max_product, ans // candidate )
            while(j < length and nums[j] == 0):
                j += 1
                flag = True
                candidate = -float('inf')
                length_later = -1
            i = j
        if flag:
            return max(max_product, 0)
        else:
            return max_product