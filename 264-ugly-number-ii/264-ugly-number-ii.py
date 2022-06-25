class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        p2,p3,p5 = 0, 0, 0
        cur_maximum = uglyNums[0]
        while(len(uglyNums) < n):
            candidate1, candidate2, candidate3 = 2*uglyNums[p2], uglyNums[p3] * 3, 5 * uglyNums[p5]
            cur_maximum = min([candidate1, candidate2, candidate3])
            #find the critical point for pointer of 2 when 2*index > cur_maximum
            uglyNums.append(cur_maximum)
            while(2*uglyNums[p2] <= cur_maximum):
                p2 += 1
            while(3*uglyNums[p3] <= cur_maximum):
                p3 += 1            
            while(5*uglyNums[p5] <= cur_maximum):
                p5 += 1
        return uglyNums[-1]
        
                
        
                        