
import pytest
import sys
sys.path.append("../")
from check_collisions import check_collisions_coins
from persons import *
from board import BOARD
import setting

def test_coins_collision():
    setting.BOARD=[]
    setting.LIVES=0
    setting.SCORE=0
    setting.COINS=[[16,40]]
    sample_mario = Mario(16,39,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[16][40]=" * "
    check_collisions_coins(" * ",1)
    assert setting.SCORE==10
