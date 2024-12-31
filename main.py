import pygame
from constants import * 
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
  dt = 0
  #
  # Game loop 
  while True:
    # set up the 'close window' button
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    # set up the screen 
    screen.fill("black")
    player.update(dt)
    player.draw(screen)
    pygame.display.flip()

    # limit the framerate to 60 FPS 
    dt =  clock.tick(60) / 1000 


if __name__ == "__main__":
  main()

