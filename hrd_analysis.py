from huarongdao import *




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
        self.record = []
        self.statTree = hrdStatus(self.game.getStatsCode())
        self.currStat = self.game.getStatsCode()
        pass


    def move(self, mv:MOVE):
        if self.game.key_to_move(mv.value):
            self.record.append(mv.value)
            self.currStat = self.game.getStatsCode()
            return True
        else:
            return False

    def replay(self, mvlist):
        for mv in mvlist:
            self.move(mv)

    def invreplay(self,mvlist):
        invmove = mvlist.copy()
        invmove.reverse()
        self.replay(invmove)





def test():
    game = Logic(4,4)
    hrd = hrdController(game)
    print(hrd.game)
    game.key_to_move('R')
    game.key_to_move('R')

    print(game.getStatsCode())
    print(genCode(10),genCode(2))



    pass

if __name__ == '__main__':
    test()