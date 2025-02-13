# 벽돌깨기 
import pygame 
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys 
import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGH = 800

class Block:
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 90

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_E(self):
        pygame.draw.ellipse(Surface, self.col, self.rect)

    def draw_R(self):
        pygame.draw.rect(Surface, self.col, self.rect)

pygame.init()
Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH)) 
FRSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Blocks!!')
pygame.key.set_repeat(10, 10)

def reset_game():
    global BALL, PADDLE, BLOCK, score, is_game_star
    score = 0
    BALL = Block((200, 200, 0), Rect(375, 650, 20, 20), 10)
    PADDLE = Block((200, 200, 0), Rect(375, 700, 100, 30))
    BLOCK = []
    colors = [(255, 0, 0), (255, 150, 0), (255, 228, 0), 
              (11, 201, 4), (0, 80, 255), (0, 0, 147),
              (201, 0, 167)]
    for y, color in enumerate(colors, start=0):
        for x in range(0, 9):
            BLOCK.append(Block(color, Rect(x * 80 + 150, y * 40 + 40, 60, 20)))
    is_game_star = False

def main():
    global is_game_star, score, BALL, PADDLE, BLOCK
    reset_game()

    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('CLEAR!!', True, 'yellow')
    M_FAIL = bigFont.render('FAILED', True, 'red')

    while True:
        M_SCORE = smallFont.render(f'SCORE : {score}', True, 'white')
        M_SPEED = smallFont.render(f'SPEED : {BALL.speed}', True, 'white')
        Surface.fill(color='black')

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    PADDLE.rect.centerx = max(PADDLE.rect.centerx - 10, 55)
                elif event.key == K_RIGHT:
                    PADDLE.rect.centerx = min(PADDLE.rect.centerx + 10, SCREEN_WIDTH - 50)
                elif event.key == K_SPACE:
                    is_game_star = True

        if not is_game_star:
            Surface.blit(M_GAME_TITLE, ((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGH / 2) - 25))
            Surface.blit(M_GAME_SUBTITLE, ((SCREEN_WIDTH / 2) - 150, (SCREEN_HEIGH / 2) + 50))
        else:
            Surface.blit(M_SCORE, (10, 770))
            Surface.blit(M_SPEED, (SCREEN_WIDTH - 220, 770))
            LenBlock = len(BLOCK)
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            if len(BLOCK) != LenBlock:
                BALL.dir *= -1
                BALL.speed += 0.25
                score += 10

            if BALL.rect.centery < 1000:
                BALL.move()

            if PADDLE.rect.colliderect(BALL.rect):
                BALL.speed += 0.25
                BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100

            if BALL.rect.centerx < 10 or BALL.rect.centerx > (SCREEN_WIDTH - 10):
                BALL.dir = 180 - BALL.dir
            elif BALL.rect.centery < 10:
                BALL.dir = -BALL.dir

            if len(BLOCK) == 0:
                Surface.blit(M_CLEAR, ((SCREEN_WIDTH / 2) - 120, (SCREEN_HEIGH / 2) - 25))
                pygame.display.update()
                pygame.time.wait(3000)
                reset_game()
            if BALL.rect.centery > 800:
                Surface.blit(M_FAIL, ((SCREEN_WIDTH / 2) - 120, (SCREEN_HEIGH / 2) - 25))
                pygame.display.update()
                pygame.time.wait(3000)
                reset_game()

            BALL.draw_E()
            PADDLE.draw_R()
            for i in BLOCK:
                i.draw_R()

        pygame.display.update()
        FRSCLOCK.tick(30)

if __name__ == '__main__':
    main()