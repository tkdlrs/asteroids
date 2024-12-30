import pygame
from constants import *  

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0  
  # Game loop 
  while True:
    # set up the 'close window' button
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    # set up the screen 
    screen.fill("black")
    pygame.display.flip()
    # 
    delta_time = clock.tick(60)
    dt = delta_time / 1000 



if __name__ == "__main__":
  main()

