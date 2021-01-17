from enum import Enum
class MOVE(Enum):
    Unknown = ''
    left = 'L'
    right = 'R'
    up = 'U'
    down = 'D'

def test():
    print(MOVE.down.value)

if __name__ == '__main__':
    test()