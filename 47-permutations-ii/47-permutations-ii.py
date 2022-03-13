class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = dict()
        result = []
        def permutation(res):
            if len(res) == n:
                result.append(res[:])
                return
            for index, num in enumerate(nums):
                if num not in visited or not visited[num]  or (visited[num][-1] < index):
                    if num not in visited:
                        visited[num]=[index]
                    else:
                        visited[num].append(index)
                    res.append(num)

                    permutation(res)
                    res.pop()
                    visited[num].pop()
        permutation([])
        return result
                    