''' method to check obstacles '''
import setting

class Bricks:
    ''' class for Bricks '''
    def __init__(self, x_variable, y_variable, string):
        self.x_variable = x_variable
        self.y_variable = y_variable
        self.string = string

    def draw(self):
        ''' function draw '''
        setting.BOARD[self.x_variable][self.y_variable] = self.string
    def check(self):
        ''' method to check for string '''
        return self.string
