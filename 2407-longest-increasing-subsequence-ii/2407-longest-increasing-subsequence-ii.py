
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        
        tree = [0] * 4 * n
        ans = 0
        
        def pointUpdate(l, r, index, idx, val):
            if (l == r == idx):
                tree[index] = max(tree[index], val)
                return
            if(idx < l or idx > r):
                return
            mid = l + (r - l) // 2
            if(idx <= mid):
                pointUpdate(l, mid, 2 * index, idx, val)
            else:
                pointUpdate(mid + 1, r, 2 * index + 1, idx, val)
            tree[index] = max(tree[2*index], tree[2*index+1])
            return
        def query(l, r, index, ql, qr):
            if(ql <= l and r <= qr):
                return tree[index]
            if(r < ql or l > qr):
                return 0
            mid = l + (r - l)//2
            leftMax = query(l, mid, 2*index, ql, qr)
            rightMax = query(mid + 1, r, 2*index+1, ql, qr)
            return max(leftMax, rightMax)
        for num in nums:
            if num == 1:
                pointUpdate(1, n, 1, num, 1)
            else:
                prevMax = query(1,  n, 1, max(num - k, 1), num - 1)
                ans = prevMax + 1
                pointUpdate(1, n, 1, num, ans)
        return tree[1]
            
        
        
        
        
            
            
        
        
        