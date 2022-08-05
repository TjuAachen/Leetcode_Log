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
   #     self.cur_food = self.food[0]
        self.score = 0
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    
    def detect_hitting(self, new_head):
        #decide the snake body and wall
        within_boundary = 0 <= new_head[1] < self.width and 0 <= new_head[0] < self.height
        bite_self = tuple(new_head) in self.snake_set and new_head != self.snake[-1]
        if not bite_self and within_boundary:
            return False
        return True
        
    def move(self, direction: str) -> int:
        old_head = self.snake[0]
        x, y = self.movement[direction]
        return self.update_score_body(old_head, x, y)
    
    def update_score_body(self, old_head, x, y):
        new_head = [old_head[0] + x, old_head[1] + y]
        #hit the wall or body
        if self.detect_hitting(new_head):
            return -1
            #update score/body/food
        if self.food and new_head == self.food[0]:  
            #update score
            self.score += 1
            #update food 
            self.food.pop(0)
        #remove tail if no food
        else:
            old_tail = self.snake.pop()
            self.snake_set.remove(tuple(old_tail))
        self.snake.appendleft(new_head)
        self.snake_set.add(tuple(new_head))
        return self.score

            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)