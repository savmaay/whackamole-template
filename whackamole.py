import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_rect = mole_image.get_rect(topleft=(0, 0))
        screen.blit(mole_image, mole_rect)
        running = True
        mole = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        new_x = random.randrange(0, 20) * 32
                        new_y = random.randrange(0, 16) * 32
                        mole_rect.topleft = (new_x, new_y)
            screen.fill("light green")
            for i in range(32):
                pygame.draw.line(screen, "blue", (i*32,0), (i*32,512))
            for i in range(32):
                pygame.draw.line(screen, "red", (0, i*32), (640, i*32))
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
