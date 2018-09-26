# 353 Design Snake Game

class Snake(object):
    def __init__(self, pos, size):
        self.pos = [pos]
    
    def getPosition(self):
        return self.pos[0]
    
    def moveTo(self, newR, newC, grow):
        if grow:
            self.pos.insert(0, (newR, newC))
        else:
            self.pos.pop()
            if (newR, newC) in self.pos:
                return False
            self.pos.insert(0, (newR, newC))
        return True
        
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.nr = height
        self.nc = width
        self.food = food
        self.snake = Snake((0, 0), 1)
        self.score = 0
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction == 'U':
            dirr = -1
            dirc = 0
        if direction == 'L':
            dirr = 0
            dirc = -1
        if direction == 'R':
            dirr = 0
            dirc = 1
        if direction == 'D':
            dirr = 1
            dirc = 0
        
        currR, currC = self.snake.getPosition()
        newR, newC = currR + dirr, currC + dirc
        
        if not (0 <= newR < self.nr and 0 <= newC < self.nc):
            return -1
              
        if self.food and newR == self.food[0][0] and newC == self.food[0][1]:
            # check if we can eat the food
            status = self.snake.moveTo(newR, newC, True)
            self.score += 1
            self.food.pop(0)
        else:
            status = self.snake.moveTo(newR, newC, False)
        
        if status:
            return self.score
        return -1
            
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)