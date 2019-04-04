''' make_clouds_in_game'''
import setting
AR = []
for i in range(80):
    AR.append(i * 5)

def make_clouds():
    '''function_to_make_clouds'''
    for j in AR:
        setting.BOARD[3][j] = "{ }"
        setting.BOARD[2][j] = "{ }"
        setting.BOARD[3][j + 1] = "{ }"
        setting.BOARD[2][j + 1] = "{ }"
