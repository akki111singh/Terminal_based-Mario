''' module to draw persons '''
import time
import setting
import draw as d

class Mario():
    ''' class mario '''
    def __init__(self, x_variable, y_variable, string, str2):
        self.x_variable = x_variable
        self.y_variable = y_variable
        self.string = string
        self.str2 = str2
        self.jumping = False
        self.jump_offset = 0

    def mario_clear_b(self):
        ''' function to clear mario backwards '''
        setting.BOARD[setting.X][setting.MARIO_POSITION - 1] = "   "

    def mario_clear_f(self):
        ''' function to clear mario forwards '''
        setting.BOARD[setting.X][setting.MARIO_POSITION + 1] = "   "

    def draw(self):
        ''' function to draw mario '''
        if setting.MARIO_POSITION % 2 == 0:
            setting.BOARD[self.x_variable][self.y_variable] = self.string
        else:
            setting.BOARD[self.x_variable][self.y_variable] = self.str2


class enemy():
    ''' class enemy '''
    def __init__(self, x_variable, y_variable, speed, sp_variable, string):
        self.x_variable = x_variable
        self.y_variable = y_variable
        self.string = string
        self.speed = speed
        self.jump_offset = 0
        self.sp_variable = sp_variable
        self.count = 0
        self.flag = 0

    def enemy_clear_b(self):
        ''' function to clear enemy backwards '''
        setting.BOARD[self.x_variable][self.y_variable - self.speed] = "   "
        setting.BOARD[self.x_variable - 1][self.y_variable - self.speed] = "   "

    def enemy_clear_f(self):
        ''' function to clear enemy forwards '''
        setting.BOARD[self.x_variable][self.y_variable + self.speed] = "   "
        setting.BOARD[self.x_variable - 1][self.y_variable + self.speed] = "   "

    def draw_enemy(self):
        ''' function to draw enemy '''
        setting.BOARD[self.x_variable][self.y_variable] = self.string
        setting.BOARD[self.x_variable - 1][self.y_variable] = "(!)"

    def move(self):
        ''' function to move objects'''
        self.y_variable += self.speed
        setting.BOARD[self.x_variable][self.y_variable] = self.string
        setting.BOARD[self.x_variable - 1][self.y_variable] = "(!)"

        if setting.BOARD[self.x_variable][self.y_variable + self.speed] == "[ ]":
            setting.BOARD[self.x_variable][self.y_variable - self.speed] = "   "
            setting.BOARD[self.x_variable - 1][self.y_variable - self.speed] = "   "

        if setting.BOARD[self.x_variable][self.y_variable + self.speed] == "   ":
            setting.BOARD[self.x_variable][self.y_variable - self.speed] = "   "
            setting.BOARD[self.x_variable - 1][self.y_variable - self.speed] = "   "
        else:
            #setting.BOARD[self.x_variable][self.y_variable+self.speed]="   "
            setting.BOARD[self.x_variable][self.y_variable - self.speed] = "   "
            setting.BOARD[self.x_variable - 1][self.y_variable - self.speed] = "   "
        self.count = 0

    def update(self):
        ''' function to update enemy '''
        if setting.BOARD[self.x_variable][self.y_variable + self.speed] == "[ ]":
            self.speed = self.speed * -1

        if setting.BOARD[self.x_variable + 1][self.y_variable + self.speed] == "   ":
            self.speed = self.speed * -1

        if setting.BOARD[self.x_variable][self.y_variable + self.speed] == " M ":
            self.speed = self.speed * -1

        if self.count == self.sp_variable:
            self.move()
        else:
            self.count += 1

    def check_enemy_collision(self):
        ''' function to check_enemy_collision '''
        if setting.X + 2 == self.x_variable and setting.MARIO_POSITION == self.y_variable:
            self.flag = 1
            setting.SCORE += 50
            setting.BOARD[setting.X + 1][setting.MARIO_POSITION] = "   "
            setting.BOARD[setting.X + 2][setting.MARIO_POSITION] = "   "


def enemy_collision():
    ''' function to clear enemy backwards '''
    for i in setting.ENEMY2:
        if setting.X == i.x_variable and setting.MARIO_POSITION == i.y_variable:
            if setting.MARIOSTR1 == "/m\\" and setting.MARIOSTR2 == "|m|":
            #setting.BOARD[setting.X-3][setting.MARIO_POSITION]=" -1"
                setting.X -= 10
                setting.MARIO_POSITION -= 3
                setting.LIFE = 1
                print("Mario dead respawning....")
                time.sleep(2)

        if setting.X == i.x_variable and setting.MARIO_POSITION == i.y_variable:
            if setting.MARIOSTR1 == "/M\\" and setting.MARIOSTR2 == "|M|":
                setting.MARIOSTR1 = "/m\\"
                setting.MARIOSTR2 = "|m|"


def check_life():
    ''' function to check_life '''
    if setting.LIFE == 1:
        setting.LIVES -= 1
        setting.LIFE = 0
