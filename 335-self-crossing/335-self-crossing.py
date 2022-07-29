from collections import deque
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        #
        prev_up, prev_left, prev_down, prev_right =[0,float('inf'), 0],[-float('inf'),0, 0],[0,-float('inf'), 0],[float('inf'),0, 0]
        cur_up, cur_left, cur_down, cur_right = [0,float('inf'), 0],[-float('inf'),0, 0],[0,-float('inf'), 0],[float('inf'),0, 0]
        cur_start = [0,0]
        directions = deque([(0,1),(-1,0),(0,-1),(1,0)])
        for i,dist in enumerate(distance):
            dx, dy = directions.popleft()
      #      print(cur_start)
            if i % 4 == 0:
                prev_up = cur_up[:]
                prev_down = cur_down[:]
                prev_left = cur_left[:]
                prev_right = cur_right[:]
             #up
            if dx == 0 and dy == 1:
                prev_start_x, prev_start_y, prev_distance = prev_left
                start_x, start_y = cur_start
                if start_y + dist >= prev_start_y >= start_y and prev_start_x - prev_distance<= start_x <= prev_start_x:
                    return True
                prev_up_x, prev_up_y, _ = prev_up
                if start_x == prev_up_x and start_y + dist >= prev_up_y:
                    return True
                cur_start[0], cur_start[-1] = start_x + dx*dist, start_y + dy*dist
                #prev_up = cur_up[:]
                cur_up = [start_x, start_y, dist]
              #  prev_up = cur_up[:]
            
            #left
            elif dx == -1 and dy == 0:
                prev_start_x, prev_start_y, prev_distance = prev_down
                start_x, start_y = cur_start
                if start_x - dist <= prev_start_x <= start_x and prev_start_y - prev_distance<= start_y <= prev_start_y:
                  #  print(1)
                    return True
                prev_up_x, prev_up_y, prev_up_distance = prev_up
                if prev_up_y <= start_y <= prev_up_y + prev_up_distance and start_x - dist <= prev_up_x <= start_x:
                 #   print(prev_up, cur_start, dist )
                   # print(2)
                    return True
                cur_start[0], cur_start[-1] = start_x + dx*dist, start_y + dy*dist
                cur_left = [start_x, start_y, dist]
             #   prev_left = cur_left[:]
                
            
            #down
            elif dx == 0 and dy == -1: 
                prev_start_x, prev_start_y, prev_distance = prev_right
                start_x, start_y = cur_start
                if start_y - dist <= prev_start_y <= start_y and prev_start_x<= start_x <= prev_start_x + prev_distance:
                    print(prev_right, cur_start, dist)
                   # print(1)
                    return True
                prev_left_x, prev_left_y, prev_left_distance = prev_left
                if prev_left_x - prev_left_distance <= start_x <= prev_left_x and start_y - dist <= prev_left_y <= start_y:
                   # print(2)
                    return True
                cur_start[0], cur_start[-1] = start_x + dx*dist, start_y + dy*dist
               # prev_down = cur_down[:]
                cur_down = [start_x, start_y, dist] 
               # prev_down = cur_down[:]
                
            #right
            elif dx == 1 and dy == 0:
                prev_start_x, prev_start_y, prev_distance = cur_up
                start_x, start_y = cur_start
                if start_x + dist >= prev_start_x >= start_x and prev_start_y <= start_y <= prev_start_y + prev_distance:
                    return True
                prev_down_x, prev_down_y, prev_down_distance = prev_down
                if prev_down_y - prev_down_distance <= start_y <= prev_down_y and start_x + dist >= prev_down_x >= start_x:
                    return True
                
                cur_start[0], cur_start[-1] = start_x + dx*dist, start_y + dy*dist
                #prev_right = cur_right[:]
                cur_right = [start_x, start_y, dist]
              #  prev_right = cur_right[:]
            directions.append((dx, dy))
        
        return False
            
            
            
        