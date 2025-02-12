import pygame # pygame 기본모듈 추가
from pygame.locals import QUIT # 종료처리 변수
import sys # 운영체제 시스템 명령

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((640,400)) ## tkinte == root.geometry("640x400")
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Pygame Basic")

def main():
    while True:
        Surface.fill(color="azure") #$ 색상을 알고있으면 사용
        # Surface.fill((255,255,255)) #  #FFFFFF = white.  #00000000 / #00FFFFFF  앞에있는 0 = alpha(투명도) 8자리일때
        for event in pygame.event.get(): # 키보드, 마우스 이벤트 체크
            if event.type ==QUIT:  # WM_DELETE_WINDOW
                pygame.quit() # Pygame을 종료
                sys.exit()    # 윈도우앱 탈출

        pygame.display.update() # 지금까지 작성코드를 윈도우창에 표시 *필수!
        FPSCLOCK.tick(30) # 30FPS 지정

if __name__ == "__main__":
    main()