import pytest
import sys
sys.path.append("../")
from check_collisions import check_collsion_powerup
from persons import *

def test_collision():
    sample_mario = Mario(16,40,"/m\\","|m|")
    sample_enemy = enemy(16,40, 1, 5, "@ @")
    sample_enemy2 = enemy(16,45,1,5,"@ @")
    collision1 = sample_mario.x_variable == sample_enemy.x_variable and sample_mario.y_variable == sample_enemy.y_variable
    collision2 = sample_mario.x_variable == sample_enemy2.x_variable and sample_mario.y_variable == sample_enemy2.y_variable

    assert collision1 is True and collision2 is False
