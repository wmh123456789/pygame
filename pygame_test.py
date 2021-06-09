import sys
import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60

BACKGROUND_COLOR = "#92877d"  # 背景颜色

def draw_main_window():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("WMH's playground")
    return screen


    pass


if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    screen = draw_main_window()
    num = 0
    while True:
        # seconds = press(False, logic, COUNT, seconds)  # 监控按键
        screen.fill(pygame.Color(BACKGROUND_COLOR))  # 填充背景
        font = pygame.font.SysFont('arialBlod', 30)
        screen.blit(font.render(str(num), True, (255, 255, 255)),(300,300))
        pygame.display.update()
        clock.tick(FPS)
        num += 1



pass