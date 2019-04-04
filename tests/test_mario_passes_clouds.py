import pytest
import sys
sys.path.append("../")
from check_collisions import check_collisions_above
from persons import *
from board import BOARD
import setting

def test_obstacles_below_while_jumping():
    setting.BOARD=[]
    setting.JUMP=True
    sample_mario = Mario(15,40,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[14][40]="{ }"

    check_collisions_above("===","[ ]","? ?")
    assert setting.JUMP is True
