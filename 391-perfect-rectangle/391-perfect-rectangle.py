class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        data = []
        for x, y, a, b in rectangles:
          #  height = b - y
            #left
            left = [x, y, b, 1]
            #right
            right = [a, y, b, -1]
            data.append(left)
            data.append(right)
        count = 0
        data.sort()
        i = 0
        n = len(data)
        
        while(i < n):
            
            init_x = data[i][0]
            left, right = [], []
            j = i
            while(j<n and data[j][0] == init_x):
                if data[j][-1] == 1:
                    if not left:
                        left.append([data[j][1], data[j][2]])
                    else:
                        if left[-1][-1] == data[j][1]:
                            left[-1][-1] = data[j][2]
                        elif left[-1][-1] < data[j][1]:
                            left.append([data[j][1], data[j][2]])         
                        else:
                            return False
                else:
                    if not right:
                        right.append([data[j][1], data[j][2]])
                    else:
                        if right[-1][-1] == data[j][1]:
                            right[-1][-1] = data[j][2]
                        elif right[-1][-1] < data[j][1]:
                            right.append([data[j][1], data[j][2]]) 
                        else:
                            return False
                j = j + 1
        #    print(i, j)
            i = j
            #left outer part
           # print(init_x, left, right)
            if left and right:
                n_right = len(right)
                for m, left_seg in enumerate(left):
                    if m < n_right and right[m] != left_seg or m >= n_right:
                        return False
                
            elif len(left) + len(right) != 1:
                return False
            else:
                count += 1
        
        return count == 2
                    
            
            