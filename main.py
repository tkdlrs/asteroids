import pygame
from constants import *  

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  # Game loop 
  while True:
    # set up the 'close window' button
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    # set up the screen 
    pygame.Surface.fill(screen, "black")
    pygame.display.flip()
  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
  main()

