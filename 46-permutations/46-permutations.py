class Solution(object):
    def permute(self, nums):
        self.result = []
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        def bfs(i, cur):
            if i == n - 1:
                self.result.append(cur[:])
                return
            for j in range(i, n):
                cur[i], cur[j] = cur[j], cur[i]
                bfs(i+1, cur)
                cur[i], cur[j] = cur[j], cur[i]
        bfs(0,nums)
        return self.result
        