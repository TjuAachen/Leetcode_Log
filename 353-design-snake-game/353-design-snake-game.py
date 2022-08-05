class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        
        #snake deque
        self.snake = deque()
        self.snake.append([0,0])
        
        #store the snake body for searching
        self.snake_set = set([(0,0)])
        self.width = width
        self.height = height
        self.food = food
        self.cur_food = self.food[0]
        self.score = 0
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        #status 1: Movable, 0: not movable
        self.status = 1
    
    
    def detect_hitting(self, new_head):
        #decide the snake body and wall
        if tuple(new_head) not in self.snake_set and 0 <= new_head[1] < self.width and 0 <= new_head[0] < self.height:
            
            return False
       # print(new_head, self.snake_set)
        return True
        
    def move(self, direction: str) -> int:
       # print(self.snake,self.snake_set, self.status, direction)
        if self.status == 0:
            return -1
        
        old_head = self.snake.popleft()
        self.snake_set.remove(tuple(old_head))
        x, y = self.movement[direction]
        self.update_score_body(old_head, x, y)
        if self.status:
            return self.score
        return -1
    
    def update_score_body(self, old_head, x, y):
        new_head = [old_head[0] + x, old_head[1] + y]
        old_tail = None
        
        #update body
        if self.snake:
            old_tail = self.snake.pop()
            self.snake_set.remove(tuple(old_tail))
            
            self.snake_set.add(tuple(old_head))
            self.snake.appendleft(old_head)
        
        #not hit the wall or body
        if not self.detect_hitting(new_head):
            #update score/body/food
            if new_head == self.cur_food:
                
                #update score
                self.score += 1
                
                #update cur_food  
                self.food.pop(0)
                if self.food:
                    self.cur_food = self.food[0]
                else:
                    self.cur_food = None
                
                #update body
                if old_tail:        
                    self.snake_set.add(tuple(old_tail))
                    self.snake.append(old_tail)
                else:
                    self.snake_set.add(tuple(old_head))
                    self.snake.appendleft(old_head)
            self.snake.appendleft(new_head)
            self.snake_set.add(tuple(new_head))

        #hit the wall or body
        else:
            self.status = 0
            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)