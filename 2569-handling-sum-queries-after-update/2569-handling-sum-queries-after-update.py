class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # type 1: flip from l to r
        # type 2: nums2[i] = nums1[i] * p + nums2[i]
        # type 3: give the sum of elements
        n = len(nums1)
        
        todo = [False] * (4 * n)
        cnt1 = [0] * (4 * n)
        
        def maintain(o):
            cnt1[o] = cnt1[o * 2] + cnt1[o * 2 + 1]
        
        def build(o, l, r):
            if l == r:
                #...
                cnt1[o] = nums1[l - 1]
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o)
        
        def do(o, l, r):
            cnt1[o] = r - l + 1 - cnt1[o]
            todo[o] = not todo[o]
        
        # 更新 [L, R]
        def update(o, l, r, L, R):
            if L <= l and r <= R:
                do(o, l, r)
                return
            m = (l + r) // 2
            
            #向下传递新值
            if todo[o]:
                do(2 * o, l, m)
                do(2 * o + 1, m + 1, r)
                todo[o] = False
            if m >= L: update(o * 2, l, m, L, R)
            if m < R: update(o * 2 + 1, m + 1, r, L, R)
            
            #维护
            maintain(o)
        
        build(1, 1, n)      
        ans = []
        s = sum(nums2)
        
        for op, l, r in queries:
         #   print(op, s, cnt1[1])
            if op == 1:
                update(1, 1, n, l + 1, r + 1)
            elif op == 2: 
                s += l * cnt1[1]
            else: 
                ans.append(s)
        
        return ans
                
        
        
                