''' module for drawing main board of game '''
from colorama import Fore
import draw as d
import setting

class BOARD:
    ''' class for the main board of game '''
    def __init__(self, board_width, board_height):
        self.height = board_height
        self.width = board_width

    def drawboard(self):
        ''' function to draw the main board '''
        horizontal_line = '==========================================================================================='
        print(Fore.BLUE + horizontal_line)
        BEGIN = setting.COUNT
        END = int(self.width) + setting.COUNT

        if setting.MARIO_POSITION > int((BEGIN + END) / 2):
            for x_values in range(self.height):
                print(Fore.BLUE + '|', end='')
                for y_values in range(BEGIN, END):
                    if setting.BOARD[x_values][y_values] == "===":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == " * ":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == setting.MARIOSTR1:
                        print(Fore.BLUE + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == setting.MARIOSTR2:
                        print(Fore.CYAN + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "###":
                        print(
                            Fore.GREEN + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "(!)":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "$$$":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "@ @":
                        print(
                            Fore.MAGENTA + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "[ ]":
                        print(Fore.BLUE + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "($)":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == " M ":
                        print(Fore.CYAN + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "(@)":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == ">5K":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == " ||":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "[!]":
                        print(Fore.CYAN + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    else:
                        print(
                            Fore.WHITE + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')

                print(Fore.BLUE + '|')
            print(Fore.BLUE + horizontal_line)
        else:
            for x_values in range(self.height):
                print('|', end='')
                for y_values in range(BEGIN, END):
                    if setting.BOARD[x_values][y_values] == "===":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == " * ":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == setting.MARIOSTR1:
                        print(Fore.BLUE + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == setting.MARIOSTR2:
                        print(Fore.CYAN + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "###":
                        print(
                            Fore.GREEN + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "$$$":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "(!)":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "@ @":
                        print(
                            Fore.MAGENTA + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "[ ]":
                        print(Fore.BLUE + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "(@)":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == ">5K":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "($)":
                        print(Fore.RED + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == " M ":
                        print(Fore.CYAN + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == " ||":
                        print(
                            Fore.YELLOW + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                    elif setting.BOARD[x_values][y_values] == "[!]":
                        print(Fore.CYAN + '%s' % (setting.BOARD[x_values][y_values]), end='')
                    else:
                        print(
                            Fore.WHITE + '%s' %
                            (setting.BOARD[x_values][y_values]), end='')
                print(Fore.BLUE + '|')
            print(Fore.BLUE + horizontal_line)
        for x_values in range(17, 22):
            for y_values in range(400):
                setting.BOARD[x_values][y_values] = "###"

    def getnewboard(self):
        ''' function_to_get_new_board '''
        for i in range(self.height):
            setting.BOARD.append(['   '] * 400)
        return setting.BOARD

    def resetboard(self):
        ''' function_to_reset_the_board '''
        for x_values in range(self.width):
            for y_values in range(self.width):
                setting.BOARD[x_values][y_values] = '  '
