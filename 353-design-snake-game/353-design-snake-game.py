class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.food = food
        self.width = width
        self.height = height
        self.snake_deque = deque([[0,0]])
        self.snake_set = set()
        self.snake_set.add((0,0))
        self.move_step = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
        self.score = 0
        
    def detect_hitting(self, new_head):
        #detect the hitting of wall
        is_hitting_wall = True
        if 0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width:
            is_hitting_wall = False
        #detect the hitting of itself
        is_hitting_self = tuple(new_head) in self.snake_set and new_head != self.snake_deque[-1]
        if is_hitting_self or is_hitting_wall:
            return True
        return False

    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        step = self.move_step[direction]
        new_head = [self.snake_deque[0][0] + step[0], self.snake_deque[0][1] + step[1]]
        if self.detect_hitting(new_head):
            return -1
        
        if self.food and self.food[0] == new_head:
            self.food.pop(0)
            self.score += 1
        else:
            old_tail = self.snake_deque.pop()
            self.snake_set.remove(tuple(old_tail))
        self.snake_deque.appendleft(new_head)
        self.snake_set.add(tuple(new_head))
        return self.score
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)