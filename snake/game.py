# coding:utf-8
# 使用pygame实现贪吃蛇

import pygame
import sys
import random

# 全局定义
SCREEN_X = 550
SCREEN_Y = 550


# 蛇类
# 点以25为单位
class Snake(object):
    # 初始化各种需要的属性 开始时默认向右 身体块*5
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addnode()

    # 无论何时都在前端增加蛇块
    def addnode(self):
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.direction == pygame.K_LEFT:
            node.left -= 25
        elif self.direction == pygame.K_RIGHT:
            node.left += 25
        elif self.direction == pygame.K_UP:
            node.top -= 25
        elif self.direction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)

    # 删除最后一个块
    def delnode(self):
        self.body.pop()

    # 死亡判断
    def isdead(self):
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 移动
    def move(self):
        self.addnode()
        self.delnode()

    # 改变方向，但是左右、上下不能被逆向改变
    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if curkey in LR and self.direction in LR:
                pass
            if curkey in UD and self.direction in UD:
                pass
            self.direction = curkey


# 食物类
class Food(object):
    def __init__(self):
        self.rect = pygame.Rect(-25, 0, 25, 25)

    def remove(self):
        self.rect.x = -25

    def set(self):
        if self.rect.x == -25:
            allpos = []
            for pos in range(25, SCREEN_X - 25, 25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)
            print(self.rect)


def show_text(screen, pos, text, color, font_bold=False, font_size=60, font_italic=False):
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体", font_size)
    # 设置是否加粗属性
    cur_font.set_bold(font_bold)
    # 设置是否斜体属性
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    screen.blit(text_fmt, pos)


# 需要添加一个启动界面，而不是一上来游戏就是进行中
def main():
    pygame.init()
    screen_size = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    scores = 0
    isdead = False

    # 蛇/食物
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                if event.key == pygame.K_SPACE and isdead:
                    return main()

        screen.fill((255, 255, 255))

        # 画蛇身 / 每一步加一分
        if not isdead:
            scores += 1
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen, (20, 220, 39), rect, 0)

        # 显示游戏结束文字
        isdead = snake.isdead()
        if isdead:
            show_text(screen, (100, 200), 'GAME OVER!', (227, 29, 18), False, 60)
            show_text(screen, (150, 300), 'press space to try again...', (0, 0, 22), False, 20)

        # 食物处理 吃到+50分
        # 当食物rect与蛇头重合，吃掉 snake增加一个Node
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()
            snake.addnode()

        # 食物刷新
        food.set()
        pygame.draw.rect(screen, (136, 0, 21), food.rect, 0)

        # 显示分数文字
        show_text(screen, (50, 500), 'Scores:' + str(scores), (223, 223, 223), False, 20)

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
