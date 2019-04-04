import pytest
import sys
sys.path.append("../")
from check_collisions import get_coin_from__brick
from persons import *
from board import BOARD
import setting

def test_get_coins_from_brick():
    setting.BOARD=[]
    setting.JUMP=True
    setting.SPECIAL_BRICK=[[14,40]]
    sample_mario = Mario(15,40,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[14][40]="? ?"

    get_coin_from__brick("? ?","???")
    assert setting.BOARD[13][40]==" * "
