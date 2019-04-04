'''module_to_control_key_functions'''
import random
import os
import input as key
import setting
from persons import Mario
import boss_enemy as b_e
import check_collisions as c_c
MARIO = Mario(
    setting.X,
    setting.MARIO_POSITION,
    setting.MARIOSTR1,
    setting.MARIOSTR2)
KEY_PRESSED = key.KBHit()


def check_pressed_key(k):
    ''' module to check key_pressing '''
    if KEY_PRESSED.kbhit():
        k = KEY_PRESSED.getch()
    else:
        k = 0
    if k == "d":
        begin = setting.COUNT
        end = 30 + setting.COUNT
        if setting.MARIO_POSITION >= (begin + end) / 2:
            setting.COUNT += 1
        c_c.check_collisions_coins(" * ", 1)
        c_c.check_collsion_powerup("$$$", 1)

        if setting.BOARD[setting.X][setting.MARIO_POSITION + 1] == "[ ]":
            MARIO.mario_clear_b()

        elif setting.BOARD[setting.X][setting.MARIO_POSITION + 1] == "TTT":
            MARIO.mario_clear_b()

        elif setting.BOARD[setting.X][setting.MARIO_POSITION + 1] == " ||":
            MARIO.mario_clear_b()

        elif c_c.check_collision_juming("==="):
            setting.JUMP = False
            MARIO.mario_clear_b()

        elif c_c.check_collision_juming("???"):
            setting.JUMP = False
            MARIO.mario_clear_b()

        elif c_c.check_collision_juming("? ?"):
            setting.JUMP = False
            MARIO.mario_clear_b()
        elif c_c.check_collision_juming("wWw"):
            setting.JUMP = False
            MARIO.mario_clear_b()
        elif c_c.check_collision_juming("(@)"):
            setting.JUMP = False
            MARIO.mario_clear_b()

        else:
            if setting.X <= 16:
                setting.MARIO_POSITION += 1
                MARIO.mario_clear_b()
    if k == "a":
        c_c.check_collisions_coins(" * ", -1)
        c_c.check_collsion_powerup("$$$", -1)

        if c_c.check_collision_juming_b("[ ]"):
            setting.JUMP = False
            MARIO.mario_clear_f()

        elif c_c.check_collision_juming_b("TTT"):
            MARIO.mario_clear_f()
        elif c_c.check_collision_juming_b("==="):
            setting.JUMP = False
            MARIO.mario_clear_f()

        elif c_c.check_collision_juming_b("???"):
            setting.JUMP = False

        elif c_c.check_collision_juming_b(" ||"):
            setting.JUMP = False

        elif c_c.check_collision_juming_b("???"):
            setting.JUMP = False

        elif c_c.check_collision_juming_b("wWw"):
            setting.JUMP = False

        elif c_c.check_collision_juming_b("(@)"):
            setting.JUMP = False
        elif c_c.check_collision_juming_b(" M "):
            setting.JUMP = False
        else:
            if setting.MARIO_POSITION > setting.COUNT and setting.X <= 16:
                setting.MARIO_POSITION -= 1
                MARIO.mario_clear_f()

    if k == "w" and setting.JUMP is False and setting.JUMP_OFFSET == 0 and setting.BOARD[
            setting.X + 1][setting.MARIO_POSITION] != "   ":
        setting.JUMP = True
        os.system('aplay ./sounds/jump.wav&')
        setting.JUMP_HEIGHT = 6

    if setting.JUMP is False and setting.JUMP_OFFSET == 0 and setting.BOARD[
            setting.X + 1][setting.MARIO_POSITION] == "TTT":
        setting.JUMP = True
        setting.JUMP_HEIGHT = 10

    c_c.check_collisions_above("===", "???", "? ?")
    if setting.JUMP and setting.BOARD[setting.X -
                                      1][setting.MARIO_POSITION] == " M ":
        setting.JUMP = False
    elif setting.JUMP and setting.BOARD[setting.X - 1][setting.MARIO_POSITION] == "wWw":
        setting.JUMP = False
    if setting.JUMP is False and setting.BOARD[setting.X +
                                               1][setting.MARIO_POSITION] != "   ":
        setting.JUMP_OFFSET = 0
        c_c.check_collsion_powerup_x("$$$", 1)
        c_c.check_collisions_coins_x(" * ", 1)

    if setting.JUMP is False and setting.BOARD[setting.X +
                                               1][setting.MARIO_POSITION] == "{ }":
        setting.JUMP_OFFSET = 1

    if setting.JUMP is False and setting.BOARD[setting.X +
                                               1][setting.MARIO_POSITION] == "($)":
        setting.BOARD[setting.X][setting.MARIO_POSITION] = "   "
        setting.X = setting.EX - 4
        setting.MARIO_POSITION -= 1
        setting.BOSS_POWER += 1
        b_e.clear_enemy(setting.EX, setting.EY)
        setting.EX = 13
        setting.EY = random.randint(177, 197)
        setting.CHECK = 0
        setting.SCORE += 150

    if setting.JUMP is False:
        if setting.BOARD[setting.X+1][setting.MARIO_POSITION] == "   " and setting.X != 16:
            setting.JUMP_OFFSET = 1
        if k == "q":
            setting.QUIT_GAME = 1


def do_jumping():
    ''' function_to_control_jumping_of_mario'''
    if setting.JUMP:
        setting.JUMP_OFFSET = setting.JUMP_OFFSET + 1
        setting.X = setting.X - 1
        setting.BOARD[setting.X][setting.MARIO_POSITION] = " m "
        setting.BOARD[setting.X + 1][setting.MARIO_POSITION] = "   "
        c_c.check_collisions_coins_x(" * ", -1)
        c_c.check_collsion_powerup_x("$$$", -1)

        if setting.JUMP_OFFSET == setting.JUMP_HEIGHT:
            setting.JUMP = False

    elif setting.JUMP_OFFSET > 0 and setting.JUMP is False:
        setting.JUMP_OFFSET -= 1
        setting.X = setting.X + 1
        setting.BOARD[setting.X][setting.MARIO_POSITION] = "|m|"
        setting.BOARD[setting.X - 1][setting.MARIO_POSITION] = "   "
        c_c.check_collisions_coins_x(" * ", 1)
        c_c.check_collsion_powerup_x("$$$", 1)
