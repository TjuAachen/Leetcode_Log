class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        left, right = matrix[0][0], matrix[-1][-1]
        
        def check(num):
            i = n - 1
            max_left, min_right = -float('inf'),float('inf')
            count = 0
            j = 0
            while(0 <= i < n and 0 <= j < n):
                if matrix[i][j] <= num:
                    max_left = max(max_left, matrix[i][j])
                    count += i + 1
                    j += 1
                    
                else:
                    min_right = min(min_right, matrix[i][j])
                    i -= 1
            return count, max_left, min_right
        
        while(left <= right):
            mid = left + (right - left) // 2
            count, max_left, min_right = check(mid)
           # print(count, mid, max_left, min_right)
            if count == k:
                return max_left
            elif count < k:
                if mid == right:
                    return min_right
                nxt_count, _, _ = check(mid + 1)
                if nxt_count <= k:
                    left = mid + 1
                else:
                    return min_right
            else:
                if mid == left:
                    return max_left
                nxt_count, _, _ = check(mid - 1)
             #   print(nxt_count, mid-1)
                if nxt_count >= k:
                    right = mid - 1
                else:
                    return max_left
            
                
                
        
        
        