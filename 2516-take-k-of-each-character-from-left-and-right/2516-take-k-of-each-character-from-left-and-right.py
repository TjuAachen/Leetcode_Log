class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        positions = defaultdict(list)
        
        n = len(s)
        self.prefix = [0] * (n + 1) 
        cur = [0] * 3
        self.prefix[0] = [0] * 3
        
        for i, char in enumerate(s):
            positions[char].append(i)
            cur[ord(char) - ord('a')] += 1
            self.prefix[i + 1] = cur[:]
        
        if len(positions) != 3 and k > 0:
            return -1
        n = len(s)
       # left, right = -1, n

        for char, index in positions.items():
            if len(index) < k:
                return -1
        
        left, right = k * 3, n - 1
        
        while(left <= right):
            mid = left + (right - left) // 2
          #  print(mid, self.check(mid, k), left, right)
            if self.check(mid, k):
                if left == mid:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def check(self, curAns, k):
        
        n = len(self.prefix) - 1
        
        for leftAns in range(curAns + 1):
            rightAns = curAns - leftAns
            leftCount = self.prefix[leftAns]
            rightCount = [0] * 3
            val = True
            for i in range(3):
             #   print(self.prefix, rightAns, n)
                rightCount[i] = self.prefix[-1][i] - self.prefix[n - rightAns][i]
                curCount = leftCount[i] + rightCount[i]
                if curCount < k:
                    val = False
            if val:
                return True
        return False
            
        
                
            
            
            