''' module to draw the view of game '''
import os
import setting
from obstacles import Bricks
from persons import enemy
setting.F = 8
setting.BRICK = [[7, 28], [7, 29], [7, 31], [7, 32], [7, 33], [12, 4], [12, 8], [12, 10],
                 [12, 12], [13, 61], [13, 63], [10, 71], [10, 70], [10, 69], [10, 68],
                 [10, 67], [10, 66], [9, 74], [9, 75], [12, 76], [12, 80], [12, 85],
                 [8, 86], [8, 87], [8, 88], [8, 89], [8, 90], [8, 91], [8, 92], [8, 93],
                 [16, 122], [16, 125], [13, 158], [9, 161], [9, 162], [9, 163], [9, 164],
                 [9, 165], [9, 168], [9, 166], [9, 167]]
setting.PIPE = [[15, 15], [16, 15], [14, 22], [15, 22], [16, 22], [14, 32],
                [15, 32], [16, 32], [14, 44], [15, 44], [14, 101], [16, 44],
                [13, 102], [14, 103], [16, 115], [15, 115], [14, 115], [14, 140],
                [15, 140], [16, 140], [16, 171], [16, 172], [16, 173], [15, 172],
                [15, 173], [14, 172], [13, 173], [14, 173], [14, 202], [15, 202], [16, 202]]

setting.SPECIAL_BRICK = [[12, 9], [7, 30], [13, 159], [12, 11], [13, 62], [9, 76]]
setting.COINS = [[6, 161], [6, 162], [6, 163], [5, 163], [4, 163], [6, 164],
                 [4, 153], [5, 153], [6, 153], [7, 153], [7, 115], [8, 115],
                 [9, 115], [10, 122], [11, 123], [10, 124], [8, 140], [9, 140],
                 [7, 140], [16, 148], [16, 149], [16, 150], [16, 110], [16, 111],
                 [16, 112], [8, 102], [7, 102], [6, 102], [5, 102], [12, 63], [8, 70],
                 [9, 69], [9, 68], [8, 74], [8, 75], [11, 80], [11, 85], [6, 86], [6, 87],
                 [6, 88], [7, 91], [7, 92], [7, 93], [16, 56], [16, 57], [16, 58], [6, 28],
                 [6, 29], [6, 31], [6, 32], [6, 33], [5, 28], [5, 29], [5, 31], [5, 32],
                 [5, 33], [11, 4], [11, 6], [11, 7], [9, 10], [10, 10], [9, 12], [10, 12],
                 [16, 17], [16, 18], [16, 19], [12, 50], [11, 50], [10, 50], [16, 36], [16, 37],
                 [16, 38], [16, 26], [15, 26]]

setting.HOLES = [[16, 50], [16, 51], [16, 70], [16, 71], [16, 100], [16, 101], [16, 102],
                 [16, 103], [16, 104], [16, 120], [16, 121], [16, 123], [16, 124],
                 [16, 126], [16, 127], [16, 200], [16, 201]]

setting.ENEMY = [[16, 14], [16, 23], [16, 33], [16, 36], [16, 50], [16, 90],
                 [16, 92], [7, 86], [16, 110], [16, 136], [16, 138], [8, 163], [8, 165]]

setting.POWERUP = [[8, 10], [5, 93], [5, 166]]

setting.FLAG = [[16, 206], [15, 206], [14, 206], [13, 206], [12, 206], [11, 206],
                [10, 206], [9, 206], [8, 206]]

setting.HOUSE = [[16, 215], [16, 216], [16, 217], [16, 220], [16, 221], [16, 222],
                 [15, 215], [15, 216], [15, 217], [15, 220], [15, 221], [15, 222],
                 [14, 216], [14, 217], [14, 218], [14, 219], [14, 220], [14, 221],
                 [14, 222], [13, 217], [13, 218], [13, 219], [13, 220], [13, 221], [12, 219]]

setting.SPRING = [[16, 25], [16, 153]]


def draw_bricks():
    ''' function to draw bricks '''
    for i in setting.BRICK:
        b_variable = Bricks(i[0], i[1], "===")
        b_variable.draw()
    for i in setting.SPECIAL_BRICK:
        s_variable = Bricks(i[0], i[1], "???")
        s_variable.draw()
    for i in setting.POWERUP:
        d_variable = Bricks(i[0], i[1], "? ?")
        d_variable.draw()
    for i in setting.SPECIAL_POWER:
        d_variable = Bricks(i[0], i[1], "$$$")
        d_variable.draw()
    for i in setting.FLAG:
        d_variable = Bricks(i[0], i[1], " ||")
        d_variable.draw()
    for i in setting.HOUSE:
        d_variable = Bricks(i[0], i[1], "[!]")
        d_variable.draw()
    for i in setting.SPRING:
        d_variable = Bricks(i[0], i[1], "TTT")
        d_variable.draw()
    setting.BOARD[setting.F][207] = ">5K"


def bring_flag_down():
    ''' function to bring_flag_down '''
    if setting.MARIO_POSITION == 205 and setting.F < 16:
        setting.F += 1
        setting.BOARD[setting.F - 1][207] = "   "
        os.system('aplay ./sounds/flagpole.wav&')
    if setting.F == 16:
        setting.SPRING.append([16, 204])


def draw_pipe():
    ''' function to draw pipes '''
    for i in setting.PIPE:
        p_variable = Bricks(i[0], i[1], "[ ]")
        p_variable.draw()


def draw_coins():
    ''' function to draw coins '''
    for i in setting.COINS:
        p_variable = Bricks(i[0], i[1], " * ")
        p_variable.draw()


def draw_holes():
    ''' function to draw holes '''
    for i in setting.HOLES:
        for y_variable in range(0, 5):
            p_variable = Bricks(i[0] + y_variable, i[1], "   ")
            p_variable.draw()


def generate_enemy():
    ''' function to generate_enemy '''
    for i in setting.ENEMY:
        p_variable = enemy(i[0], i[1], 1, 5, "@ @")
        setting.ENEMY2.append(p_variable)


def draw_e():
    ''' function to draw enemy'''
    for i in setting.ENEMY2:
        i.draw_enemy()


def update_enemy():
    ''' function to update_enemy '''
    for i in setting.ENEMY2:
        i.update()


def remove_enemy():
    ''' function to remove_enemy'''
    for i in setting.ENEMY2:
        i.check_enemy_collision()
        setting.ENEMY2 = [item for item in setting.ENEMY2 if item.flag != 1]


def remove_coin(x_variable, y_variable):
    ''' function to remove coins'''
    setting.COINS.remove([x_variable, y_variable])
