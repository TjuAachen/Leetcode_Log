class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        num1, num2 = tops[0], bottoms[0]
        n = len(tops)
        num = [num1,num2]
        res = []
        for j in range(4):
            if j < 2:
                time = 0
            else:
                time = 1
            i = 1
            while(i < n):
                if (tops[i] != num[j%2] and bottoms[i] != num[j%2]):
                    time = -1
                    break
                elif j == 1 and tops[i] == num[j%2] and bottoms[i] != num[j%2]:
                    time += 1
                elif j == 0 and tops[i] != num[j%2] and bottoms[i] == num[j%2]:
                    time += 1
                elif j == 2 and tops[i] == num[j%2] and bottoms[i] != num[j%2]:
                    time += 1
                elif j == 3 and tops[i] != num[j%2] and bottoms[i] == num[j%2]:
                    time += 1
                i = i + 1
            if time != -1:
                res.append(time)
        if res:
            return min(res)
        else:
            return -1
                    
        
        