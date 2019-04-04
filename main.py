''' main module to run mario '''
import time
import os
from colorama import Back, Style
import setting
from board import BOARD
import persons as p
import draw as d
from persons import Mario
import key_func as kf
import scene as sc
import check_collisions as c_c
import input as key
from boss_enemy import BossEnemy
KEY_PRESSED = key.KBHit()
B = BOARD(30, 22)
K = [0]
PRIN = [0]
GAMEBOARD = B.getnewboard()
B.drawboard()
sc.make_clouds()
d.generate_enemy()

CLOCK = time.time()
os.system('aplay ./sounds/main_theme.wav&')


def level1():
    ''' function for running level1 of the game'''
    while 1:
        clock1 = time.time()
        if setting.QUIT_GAME == 1:
            os.system('killall aplay')
            print('GAME QUIT')
            break
        if setting.MARIO_POSITION == 218:
            os.system('killall aplay')
            os.system('aplay ./sounds/stage_clear.wav')
            print(Back.CYAN + "LEVEL COMPLETED")
            print(Style.RESET_ALL)
            break

        if setting.LIVES == 0:
            os.system('killall aplay')
            os.system('aplay ./sounds/death.wav&')
            print(Back.CYAN + "GAME OVER")
            print(Style.RESET_ALL)
            break

        if 500 - int(clock1 - CLOCK) == 0:
            print(Back.CYAN + "TIME OVER")
            print(Style.RESET_ALL)
            break

        if setting.CHECK == 0:
            b_e = BossEnemy(setting.EX, setting.EY)
            setting.CHECK = 1

        if setting.BOSS_POWER == 3:
            setting.BOSS_KILLED = 1

        if setting.BOSS_POWER < 3:
            b_e.attack()

        if setting.MARIO_POSITION > 198 and setting.BOSS_KILLED == 0:
            setting.BOARD[setting.X][setting.MARIO_POSITION] = "   "
            setting.COUNT = 173
            setting.MARIO_POSITION = 173
            PRIN[0] = 1

        c_c.check_hole()
        p.check_life()
        p.enemy_collision()
        os.system('clear')
        print("SCORE= ", setting.SCORE, end="    ")
        print("LIVES=  ", setting.LIVES, end="    ")
        if setting.MARIO_POSITION > 173 and setting.MARIO_POSITION < 199:
            print("Boss=  ", 3 - setting.BOSS_POWER, end="    ")
        print("Time=  ", 150 - int(clock1 - CLOCK))
        if PRIN[0] == 1 and setting.BOSS_POWER < 3:
            print("KILL THE BOSS ENEMY FIRST")
        GAMEBOARD = B.getnewboard()
        sc.make_clouds()
        d.bring_flag_down()
        d.draw_bricks()

        if setting.BOSS_POWER < 3:
            b_e.draw_enemy()

        kf.check_pressed_key(K[0])
        kf.do_jumping()
        mario = Mario(
            setting.X,
            setting.MARIO_POSITION,
            setting.MARIOSTR1,
            setting.MARIOSTR2)
        mario.draw()
        d.draw_pipe()
        d.draw_coins()
        d.draw_e()
        d.draw_holes()
        c_c.hole()
        d.remove_enemy()
        d.update_enemy()
        B.drawboard()
        c_c.remove_special_coin()

        time.sleep(.07)


level1()
