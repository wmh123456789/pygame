from enum import Enum
from huarongdao import *

class MOVE(Enum):
    Unknown = '?'
    left = 'L'
    right = 'R'
    up = 'U'
    down = 'D'

def invMove(move):
    if move == MOVE.up:
        return MOVE.down
    elif move == MOVE.down:
        return MOVE.up
    elif move == MOVE.right:
        return MOVE.left
    elif move == MOVE.left:
        return MOVE.right
    else:
        return MOVE.unknown

class hrdStatus(object):
    def __init__(self, stat_code):
        self.code = stat_code
        self.father = None
        self.fathermove = MOVE.Unknown
        self.children = {}
        self.childrenmove = {}
        self.stepCnt = -1

    def setFather(self, father):
        self.father = father

    def addChild(self, child, move):
        self.children.update({child.code:child})
        self.childrenmove.update({child.code:move})

    def dumpMoves(self):
        stat = self
        move_str = ''
        while stat.father:
            move_str += stat.fathermove.value


class hrdController(object):
    def __init__(self, logic):
        self.game = logic
        self.game.init_load()

        pass


def main():
    game = Logic()
    hrd = hrdController(game)
    print(hrd.game)
    game.key_to_move('R')
    game.key_to_move('R')




    pass

if __name__ == '__main__':
    main()