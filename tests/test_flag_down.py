import pytest
import sys
sys.path.append("../")
from draw import bring_flag_down
from persons import *
from board import BOARD
import setting

def test_pass_bring_flag_down():
    setting.BOARD=[]
    setting.F=14
    sample_mario = Mario(15,205,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,400)
    board.getnewboard()

    bring_flag_down()
    assert setting.BOARD[13][207]== "   " and setting.F==15

def test_fail_bring_flag_down():
    setting.BOARD=[]
    setting.F=14
    sample_mario = Mario(15,200,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,400)
    board.getnewboard()

    bring_flag_down()
    assert setting.F==14
