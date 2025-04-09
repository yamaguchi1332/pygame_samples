import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("pygame demo - window title here")

running = True
x1, y1 = 0, 2

# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((238, 238, 10))  # back ground color

    pygame.draw.circle(screen, (176, 176, 50), (65, 40), 120)
    pygame.draw.circle(screen, (222, 176, 4), (75, 0), 210)
    pygame.draw.circle(screen, (222, 176, 240), (190, 10), 152)
    pygame.draw.rect(screen, (120, 120, 0), Rect(120, 120, 200, 120))

    color_on = (240, 120, 120)
    color_off = (120, 120, 120)
    for x0 in range(5):
        for y0 in range(7):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
    x1 += 1
    if x1 > 7:
        x1 = 3

    pygame.display.flip()  # update
    clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
