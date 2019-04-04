'''module for taking inputs'''
import os
import sys
import termios
import atexit
from select import select


class KBHit:
    ''' class for checking button pressed '''
    def __init__(self):
        if os.name == 'nt':
            pass
        else:
            self.fd_variable = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd_variable)
            self.old_term = termios.tcgetattr(self.fd_variable)

            self.new_term[3] = (
                self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd_variable, termios.TCSAFLUSH, self.new_term)
            atexit.register(self.set_normal_term)

    def set_normal_term(self):
        ''' function set_normal_term '''
        termios.tcsetattr(self.fd_variable, termios.TCSAFLUSH, self.old_term)
    @staticmethod
    def getch():
        ''' function getch '''
        return sys.stdin.read(1)

    @staticmethod
    def getarrow():
        ''' function get_arrow '''
        vals = [72, 77, 80, 75]
        c_variable = sys.stdin.read(3)[2]
        vals = [65, 67, 66, 68]
        return vals.index(ord(c_variable.decode('utf-8')))
    @staticmethod
    def kbhit():
        ''' function kbhit '''
        dr_variable, dw_variable, de_variable = select([sys.stdin], [], [], 0)
        dw_variable = 0
        de_variable = 0
        if dw_variable is 0:
            return dr_variable != []
        return de_variable != []
