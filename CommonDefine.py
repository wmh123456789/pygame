from enum import Enum

FPS = 60
# SHAPE = 4  # 棋盘shape
SHAPE_H = 2 # 矩形棋盘高
SHAPE_W = 4 # 矩形棋盘宽
CELL_SIZE = 100  # 方格大小
CELL_GAP_SIZE = (int)(0.08*CELL_SIZE)  # 方格间距
BORDER_R = (int)(0.15*CELL_SIZE) # 方格圆角半径
MARGIN = (int)(0.08*CELL_SIZE)  # 方格的margin
PADDING = (int)(0.08*CELL_SIZE)  # 方格的padding
SCREEN_WIDTH = (CELL_SIZE + MARGIN) * SHAPE_W + MARGIN  # 屏幕宽度
SCREEN_HEIGHT = (CELL_SIZE + MARGIN) * SHAPE_H + MARGIN  # 屏幕高度

BACKGROUND_COLOR = "#92877d"  # 背景颜色
BACKGROUND_EMPTY_CELL_COLOR = "#9e948a"  # 空方格颜色
BACKGROUND_CELL_COLOR = "#edc22e"  # 方格颜色

# 定义移动
class MOVE(Enum):
    Unknown = '?'
    left = 'L'
    right = 'R'
    up = 'U'
    down = 'D'

# 定义两个元组相加
def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

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

def genCode(num):
    return '{:X}'.format(num)
