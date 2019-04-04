import pytest
import sys
sys.path.append("../")
from check_collisions import check_collisions_below
from persons import *
from board import BOARD
import setting

def test_obstacles_below_while_jumping():
    setting.BOARD=[]
    setting.JUMP=False
    setting.JUMP_OFFSET=10
    setting.COINS=[[16,40]]
    sample_mario = Mario(15,40,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[16][40]="==="

    check_collisions_below("===","[ ]")
    assert setting.JUMP_OFFSET ==0
