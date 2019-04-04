''' module to draw boss enemy '''
import setting
from persons import enemy

class BossEnemy:
    ''' class for boss enemy '''
    def __init__(self, x_variable, y_variable):
        self.x_variable = x_variable
        self.y_variable = y_variable
        self.count = 0
        self.flag = 0

    def draw_enemy(self):
        ''' draw function for boss enemy '''
        setting.BOARD[self.x_variable - 1][self.y_variable] = "($)"
        setting.BOARD[self.x_variable][self.y_variable] = "wWw"
        setting.BOARD[self.x_variable][self.y_variable + 1] = "wWw"
        setting.BOARD[self.x_variable][self.y_variable - 1] = "wWw"
        setting.BOARD[self.x_variable - 1][self.y_variable + 1] = "(@)"
        setting.BOARD[self.x_variable - 1][self.y_variable - 1] = "(@)"
        setting.BOARD[self.x_variable + 1][self.y_variable - 1] = " M "
        setting.BOARD[self.x_variable + 1][self.y_variable + 1] = " M "

    def attack(self):
        ''' attack function for boss enemy '''
        if self.count % 100 == 0:
            setting.ENEMY2.append(enemy(self.x_variable + 3, self.y_variable, -1, 5, "OOO"))
        self.count += 1


def clear_enemy(x_variable, y_variable):
    ''' clear enemy function for boss enemy'''
    setting.BOARD[x_variable][y_variable] = "   "
    setting.BOARD[x_variable - 1][y_variable] = "   "
    setting.BOARD[x_variable + 1][y_variable] = "   "
    setting.BOARD[x_variable][y_variable + 1] = "   "
    setting.BOARD[x_variable - 1][y_variable + 1] = "   "
    setting.BOARD[x_variable + 1][y_variable + 1] = "   "
    setting.BOARD[x_variable][y_variable - 1] = "   "
    setting.BOARD[x_variable - 1][y_variable - 1] = "   "
    setting.BOARD[x_variable + 1][y_variable - 1] = "   "
