class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0:
            return 0
        n = len(citations)
        def check(i):
            real_index = n -i
            cur_h = citations[real_index]
            if cur_h >= i:
                return True
            return False
        left, right = 1, n
        while(left <= right):
            mid = left + (right - left) // 2
            if check(mid):
                if right == mid:
                    return mid
                elif check(mid+1):
                    left = mid + 1
                else:
                    return mid
            else:
                right = mid - 1
        
                    
        
                