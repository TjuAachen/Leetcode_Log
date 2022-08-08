from sortedcontainers import SortedSet
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        #
        nrow, ncol = len(matrix), len(matrix[0])
        def find_element(rowSum):
            sorted_sum = SortedSet([0])
            ans = -float('inf')
            running_sum = 0
            for num in rowSum:
                running_sum += num
                target = running_sum - k
                celing_index = sorted_sum.bisect_left(target)
                if celing_index < len(sorted_sum):
                    ans = max(ans, running_sum - sorted_sum[celing_index])
                sorted_sum.add(running_sum)
                if ans == k:
                    return ans
              #  print(ans, running_sum,sorted_sum[celing_index])
           # print(sorted_sum)
            return ans
        final_ans = -float('inf')
        for start_row in range(nrow):
            rowSum = [0] * ncol
            for cur_row in range(start_row, nrow):
                for col in range(ncol):
                    rowSum[col] += matrix[cur_row][col]
             #   print(rowSum)
                final_ans = max(final_ans, find_element(rowSum))
                if final_ans == k:
                    return final_ans
        return final_ans
                    