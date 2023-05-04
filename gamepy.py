import pygame
import math

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
pygame.init()
#pygame.mouse.set_visible(False)
LEFT = 1
SCROLL = 2
RIGHT = 3

size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

# -- bg color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 242, 0)
BLACK = (0, 0, 0)

bg = pygame.image.load('cloud.png')
screen.blit(bg, (0, 0))
bg_image = pygame.image.load('cloud.png').convert()
screen.blit(bg_image, [0, 0])
pygame.display.flip()

# -- image
# IMAGE = 'exa.jpg'
# img = pygame.image.load(IMAGE)
# screen.blit(img, (0, 0))
# pygame.display.flip()

# -- draw line
# pyGame.draw.line(surface, color, start_pos, end_pos, width=1)

MIDYPOS = 249
MIDXPOS = 199

# -- draw "sun"
# for i in range(100):
#     pygame.draw.line(screen, YELLOW, [MIDXPOS, MIDYPOS], [MIDXPOS + 350*math.sin(i*3.6), MIDYPOS + 350*math.cos(i*3.6)], 3)

# -- draw circle
# for i in range(360):
#     pygame.draw.line(screen, RED, [MIDXPOS, MIDYPOS], [MIDXPOS + 35*math.sin(i*1), MIDYPOS + 35*math.cos(i*1)], 4)


#------------GAME------------------------------------------------
RADIUS = 30
IMAGE = 'plane.png'

img = pygame.image.load(IMAGE)
player_image = pygame.image.load('plane.png').convert()
player_image.set_colorkey(YELLOW)
#screen.blit(player_image, [220, 300])
pygame.display.flip()


clock = pygame.time.Clock()
REFRESH_RATE = 60
clock = pygame.time.Clock()
x_pos = MIDXPOS
y_pos = MIDYPOS
finish = False

#-- pingpog plane
# addx = 2
# addy = 2
# while not finish:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             finish = True
#
#     screen.blit(bg, (0, 0))
#
#     if(x_pos >= WINDOW_WIDTH - 50 or x_pos <= 0):
#         addx*= -1
#     if (y_pos >= WINDOW_HEIGHT -30 or y_pos <= 0):
#         addy *= -1
#     x_pos += addx
#     y_pos += addy
#
#     screen.blit(player_image, [x_pos, y_pos])
#     pygame.display.flip()
#     clock.tick(REFRESH_RATE)
# #
# pygame.display.flip()


#--moving mouse plane
# finish = False
# pygame.mouse.set_visible(False)
#
# while not finish:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             finish = True
#     screen.blit(bg, (0, 0))
#     mouse_point = pygame.mouse.get_pos()
#     screen.blit(player_image, mouse_point)
#
#     pygame.display.flip()
#     clock.tick(REFRESH_RATE)


# #-- clicking plane
finish = False
mouse_pos_list = []
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and event.button == LEFT:
                mouse_pos_list.append(pygame.mouse.get_pos())

            screen.blit(bg, (0, 0))
            pygame.display.flip()
            for pos in mouse_pos_list:
                screen.blit(player_image, pos)
                pygame.display.flip()

    pygame.display.flip()
    clock.tick(REFRESH_RATE)







# finish = False
# while not finish:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             finish = True

pygame.quit()