import pytest
import sys
sys.path.append("../")
from check_collisions import check_collision_juming
from persons import *
from board import BOARD
import setting

def test_jumping_collision():
    setting.BOARD=[]
    setting.COINS=[[16,40]]
    sample_mario = Mario(16,39,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[16][40]="==="
    col_jump=check_collision_juming("===")
    assert col_jump is True
