import pytest
import sys
sys.path.append("../")
from check_collisions import hole
from persons import *
from board import BOARD
import setting

def test_hole_pass():
    setting.BOARD=[]
    setting.LIVES=1;
    sample_mario = Mario(16,39,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[17][40]="  "
    hole()
    assert setting.LIVES==0
def test_hole_fail():
    setting.BOARD=[]
    setting.LIVES=1;
    sample_mario = Mario(15,39,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[17][40]="  "
    hole()
    assert setting.LIVES==1
