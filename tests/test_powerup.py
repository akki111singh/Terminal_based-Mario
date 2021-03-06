import pytest
import sys
sys.path.append("../")
from check_collisions import check_collsion_powerup
from persons import *
from board import BOARD
import setting

def test_powerup():
    setting.BOARD=[]
    setting.LIVES=0
    setting.SCORE=0
    setting.SPECIAL_POWER=[[16,40]]
    sample_mario = Mario(16,39,"/m\\","|m|")
    setting.X=sample_mario.x_variable
    setting.MARIO_POSITION=sample_mario.y_variable
    board=BOARD(50,50)
    board.getnewboard()
    setting.BOARD[16][40]="$$$"
    check_collsion_powerup("$$$",1)
    assert setting.LIVES==1 and setting.SCORE==100 and setting.MARIOSTR1=="/M\\" and setting.MARIOSTR2=="|M|"
