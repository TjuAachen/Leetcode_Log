from sortedcontainers import SortedList
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        nrow, ncol = len(matrix), len(matrix[0])
        
        range_sum = [[0] * ncol for _ in range(nrow)]
        
        for i in range(nrow):
            for j in range(ncol):
                if i == 0 and j == 0:
                    range_sum[i][j] = matrix[i][j]
                elif i == 0:
                    range_sum[i][j] = range_sum[i][j-1] + sum([matrix[k][j] for k in range(i+1)])
                else:
                    range_sum[i][j] = range_sum[i-1][j] + sum([matrix[i][k] for k in range(j+1)])
        
        
        record = defaultdict(SortedList)
        
        ans = 0
        for i in range(ncol):
            for j in range(i+1):
                key = (j,i)
                cur_sum = 0
                record[key].add(cur_sum)
                for layer in range(nrow):
                    if j > 0 and layer > 0:
                        cur_layer_sum = range_sum[layer][i] - range_sum[layer][j-1] + range_sum[layer-1][j-1] - range_sum[layer-1][i]
                    elif layer > 0:
                        cur_layer_sum = range_sum[layer][i] - range_sum[layer-1][i]
                    elif j > 0:
                        cur_layer_sum = range_sum[layer][i] - range_sum[layer][j-1]
                    else:
                        cur_layer_sum = range_sum[layer][i]
                    cur_sum += cur_layer_sum
                    #not selected previous rows

                    #selected previous rows
                    new_target = cur_sum - target
                    one_ans = record[key].count(new_target)
                    ans += one_ans
                    record[key].add(cur_sum)
        return ans
        
        
        