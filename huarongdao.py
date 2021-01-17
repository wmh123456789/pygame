# https://zhuanlan.zhihu.com/p/120931476
# -*- coding: utf-8 -*-
import sys
import random
from collections import OrderedDict
import pygame
from CommonDefine import *


class Logic:
    def __init__(self, shape_h=4, shape_w=4):
        # self.shape = int(shape) if shape > 2 else 4  # 初始化形状
        self.shape_h = shape_h
        self.shape_w = shape_w
        self.tiles = OrderedDict()  # 初始化数据
        self.stepCnt = 0
        self.neighbors = [  # 定义方向矢量
            [1, 0],  # 下
            [-1, 0],  # 上
            [0, 1],  # 右
            [0, -1],  # 左
        ]
        self.click_dict = {'x': {}, 'y': {}}  # 定义鼠标点击坐标转换下标的数据
        self.init_load()  # 初始化加载

    def __str__(self):
        game_str = 'Game after {} steps \n'.format(self.stepCnt)
        for row in range(self.shape_h):
            line_str = ''
            for col in range(self.shape_w):
                line_str += '{:02} '.format(self.tiles[(row, col)])
            game_str += line_str + '\n'
        return game_str

    def getStatsCode(self):
        code = ''
        for row in range(self.shape_h):
            for col in range(self.shape_w):
                code += genCode(self.tiles[(row, col)])
        return code

    def init_load(self):
        count = 1
        # 生成正确的序列
        for x in range(self.shape_h):
            for y in range(self.shape_w):
                mark = tuple([x, y])
                self.tiles[mark] = count
                count += 1
        self.tiles[mark] = 0
        self.empty = mark
        self.stepCnt = 0


    def shuffleTiles(self, n=200):
        mark = self.empty
        for count in range(n):  # 随机移动n次
            neighbor = random.choice(self.neighbors)
            spot = tuple_add(mark, neighbor)

            if spot in self.tiles:
                number = self.tiles[spot]
                self.tiles[spot] = 0
                self.tiles[mark] = number
                mark = spot
        self.init_click_dict()
        self.empty = mark

    def init_click_dict(self):
        # 初始化点击坐标转换下标的数据
        for r in range(self.shape_h):
            for c in range(self.shape_w):
                x = MARGIN * (c + 1) + c * CELL_SIZE
                x1 = x + CELL_SIZE
                click_x = tuple(range(x, x1))

                self.click_dict['x'][click_x] = c
                y = MARGIN * (r + 1) + r * CELL_SIZE
                y1 = y + CELL_SIZE
                click_y = tuple(range(y, y1))
                self.click_dict['y'][click_y] = r

    # move for click
    def move(self, mark):
        # 移动数据
        for neighbor in self.neighbors:
            spot = tuple_add(mark, neighbor)
            # If click is available, exchange tile of clicked one and empty one
            if spot in self.tiles and self.tiles[spot] is 0:
                self.tiles[spot], self.tiles[mark] = self.tiles[mark], self.tiles[spot]
                self.empty = mark
                self.stepCnt += 1
                break

    # move for keydown
    def move2(self, neighbor):
        spot = tuple_add(neighbor, self.empty)
        if spot in self.tiles:
            self.tiles[spot], self.tiles[self.empty] = self.tiles[self.empty], self.tiles[spot]
            self.empty = spot
            self.stepCnt += 1
            return True
        else:
            return False

    def click_to_move(self, x, y):
        # 点击移动
        x1 = None
        for k, v in self.click_dict['x'].items():
            if x in k:
                x1 = v

        if x1 is None:
            return
        y1 = None
        for k, v in self.click_dict['y'].items():
            if y in k:
                y1 = v

        if y1 is None:
            return
        self.move((y1, x1))

    def key_to_move(self, direction):
        if direction in ['L', 'left']:
            return self.move2((0, 1))
        elif direction in ['R', 'right']:
            return self.move2((0, -1))
        elif direction in ['U', 'up']:
            return self.move2((1, 0))
        elif direction in ['D', 'down']:
            return self.move2((-1, 0))
        else:
            print("Invalid direction: {}".format(direction))
            return False
        pass

    def is_win(self):
        # 游戏结束判定
        if self.tiles[(self.shape_h - 1, self.shape_w - 1)] is not 0:
            return False
        values = list(self.tiles.values())
        for index in range(values.__len__() - 1):
            if index + 1 != values[index]:
                return False
        return True


def init_game():
    # 初始化游戏
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('数字华容道 -- 0')
    return screen


def draw_num(logic, screen):
    for r in range(logic.shape_h):
        for c in range(logic.shape_w):
            num = logic.tiles[(r, c)]
            if num is not 0:
                color = pygame.Color(BACKGROUND_CELL_COLOR)
            else:
                color = pygame.Color(BACKGROUND_EMPTY_CELL_COLOR)

            x = MARGIN * (c + 1) + c * CELL_SIZE
            y = MARGIN * (r + 1) + r * CELL_SIZE
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE),
                             border_radius=BORDER_R)
            if num is not 0:
                font_size = int((CELL_SIZE - PADDING) / 1.3)
                font = pygame.font.SysFont('arialBlod', font_size)
                font_width, font_height = font.size(str(num))
                screen.blit(font.render(str(num), True, (255, 255, 255)),
                            (x + (CELL_SIZE - font_width) / 2, y +
                             (CELL_SIZE - font_height) / 2 + 5))


def press(is_game_over, logic, COUNT, counts):
    for event in pygame.event.get():
        if event.type == COUNT and not is_game_over:  # 设置定时器，记录时间
            counts += 1
            pygame.display.set_caption('数字华容道 -- {}'.format(counts))
        if event.type == pygame.QUIT:  # 点击关闭按钮退出
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标点击
            if event.button == 1 and not is_game_over:
                x, y = event.pos
                logic.click_to_move(int(x), int(y))  # 点击移动
        elif event.type == pygame.KEYDOWN:
            if event.key in [ord('d'), 1073741904]:
                print('Press LEFT')
                logic.key_to_move('left')
            elif event.key in [ord('a'), 1073741903]:
                print('Press RIGHT')
                logic.key_to_move('right')
            elif event.key in [ord('s'), 1073741906]:
                print('Press UP')
                logic.key_to_move('up')
            elif event.key in [ord('w'), 1073741905]:
                print('Press DOWN')
                logic.key_to_move('down')
            elif event.key in [ord('p')]:
                print('Init Game')
                logic.init_load()
                logic.shuffleTiles()
            elif event.key == 13:  # 游戏结束，回车重开
                return True
    if COUNT:
        return counts


def game_win(screen, logic, clock, text='You Win!'):
    font = pygame.font.SysFont('Blod', int(SCREEN_WIDTH / 4))
    font_width, font_height = font.size(str(text))
    while True:
        if press(True, logic, None, None):
            break
        screen.fill(pygame.Color(BACKGROUND_COLOR))
        draw_num(logic, screen)
        screen.blit(font.render(str(text), True, (0, 0, 0)),
                    ((SCREEN_WIDTH - font_width) / 2,
                     (SCREEN_HEIGHT - font_height) / 2))
        pygame.display.update()
        clock.tick(FPS)


def main():
    screen = init_game()
    clock = pygame.time.Clock()
    logic = Logic(SHAPE_H,SHAPE_W)
    logic.shuffleTiles(200)  # 初始化开局：随机移动n次
    COUNT = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNT, 1000)
    seconds = 0  # 记录时间
    while True:
        if logic.is_win():  # 判断游戏是否胜利
            break
        seconds = press(False, logic, COUNT, seconds)  # 监控按键
        screen.fill(pygame.Color(BACKGROUND_COLOR))  # 填充背景
        draw_num(logic, screen)  # 画数字
        pygame.display.update()
        clock.tick(FPS)
    game_win(screen, logic, clock, text='Time:' + str(seconds))


if __name__ == "__main__":
    while True:
        main()
