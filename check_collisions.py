''' module to check collisions'''
import time
import os
import setting
import draw as d


def check_collision_juming(string):
    ''' function to check collisions while jumping right'''
    if setting.BOARD[setting.X][setting.MARIO_POSITION + 1] == string:
        return True


def check_collision_juming_b(string):
    ''' function to check collisions while jumping left '''
    if setting.BOARD[setting.X][setting.MARIO_POSITION - 1] == string:
        return True


def check_collisions_coins(string, y_variable):
    ''' function to check collision of coins '''
    if setting.BOARD[setting.X][setting.MARIO_POSITION + y_variable] == string:
        os.system('aplay ./sounds/coin.wav&')
        setting.SCORE += 10
        d.remove_coin(setting.X, setting.MARIO_POSITION + y_variable)


def check_collisions_coins_x(string, y_variable):
    ''' function to check collision of coins'''
    if setting.BOARD[setting.X + y_variable][setting.MARIO_POSITION] == string:
        setting.SCORE += 10
        os.system('aplay ./sounds/coin.wav&')
        d.remove_coin(setting.X + y_variable, setting.MARIO_POSITION)
        setting.BOARD[setting.X + y_variable][setting.MARIO_POSITION] = "   "


def check_collsion_powerup(string, y_variable):
    ''' function to check collision of powerups '''
    if setting.BOARD[setting.X][setting.MARIO_POSITION + y_variable] == string:
        setting.SCORE += 100
        setting.MARIOSTR1 = "/M\\"
        setting.MARIOSTR2 = "|M|"
        setting.LIVES+=1;
        setting.SPECIAL_POWER.remove([setting.X, setting.MARIO_POSITION + y_variable])
        setting.BOARD[setting.X + y_variable][setting.MARIO_POSITION] = "   "


def check_collsion_powerup_x(string, y_variable):
    ''' function to check collision of powerup '''
    if setting.BOARD[setting.X + y_variable][setting.MARIO_POSITION] == string:
        setting.SCORE += 100
        setting.MARIOSTR1 = "/M\\"
        setting.MARIOSTR2 = "|M|"
        setting.LIVES+=1;
        setting.SPECIAL_POWER.remove([setting.X + y_variable, setting.MARIO_POSITION])
        setting.BOARD[setting.X + y_variable][setting.MARIO_POSITION] = "   "


def check_collisions_above(string, str2, str3):
    ''' function to check upper collision '''
    if setting.JUMP and setting.BOARD[setting.X -
                                      1][setting.MARIO_POSITION] == string:
        setting.JUMP = False
    elif setting.JUMP and setting.BOARD[setting.X - 1][setting.MARIO_POSITION] == str2:
        setting.JUMP = False
    elif setting.JUMP and setting.BOARD[setting.X - 1][setting.MARIO_POSITION] == str3:
        setting.JUMP = False

    if setting.BOARD[setting.X - 1][setting.MARIO_POSITION] == str3:
        setting.POWERUP.remove([setting.X - 1, setting.MARIO_POSITION])
        setting.BRICK.append([setting.X - 1, setting.MARIO_POSITION])
        setting.SPECIAL_POWER.append([setting.X - 2, setting.MARIO_POSITION])

    check_collsion_powerup_x("$$$", -1)
    check_collisions_coins_x(" * ", -1)
    get_coin_from__brick("???", " * ")


def check_collisions_below(string, str2):
    ''' function to check lower collisions '''
    if setting.JUMP is False and setting.BOARD[setting.X +
                                               1][setting.MARIO_POSITION] == string:
        setting.JUMP_OFFSET = 0
    elif setting.JUMP is False and setting.BOARD[setting.X + 1][setting.MARIO_POSITION] == str2:
        setting.JUMP_OFFSET = 0
    check_collisions_coins_x(" * ", 1)
    check_collsion_powerup_x("$$$", 1)


def get_coin_from__brick(string, str2):
    ''' function to get coins from brick '''
    if setting.BOARD[setting.X - 1][setting.MARIO_POSITION] == string:
        setting.SPECIAL_BRICK.remove([setting.X - 1, setting.MARIO_POSITION])
        setting.BRICK.append([setting.X - 1, setting.MARIO_POSITION])

        setting.BOARD[setting.X - 2][setting.MARIO_POSITION] = " * "
        setting.SPECIAL_COIN.append([setting.X - 2, setting.MARIO_POSITION])


def remove_special_coin():
    ''' function to remove special coins '''
    if len(setting.SPECIAL_COIN) != 0:
        for i in setting.SPECIAL_COIN:
            setting.BOARD[i[0]][i[1]] = "   "


def hole():
    ''' function to make obstacle hole '''
    if setting.BOARD[setting.X +
                     1][setting.MARIO_POSITION] == "   " and setting.X == 16:
        setting.BOARD[setting.X][setting.MARIO_POSITION] = "   "
        setting.X = setting.X + 1
        for i in range(3):
            setting.BOARD[setting.X + 4][setting.MARIO_POSITION] = "|m|"
        setting.LIVES = setting.LIVES - 1


def check_hole():
    ''' function to check obstacle hole '''
    if setting.X >= 17:
        setting.X = 16
        setting.X = setting.X - 8
        setting.MARIO_POSITION = setting.MARIO_POSITION + 2
        print("Mario dead respawning....")
        time.sleep(2)
