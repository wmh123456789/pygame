from huarongdao import *
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