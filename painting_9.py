import pygame
from pygame.draw import *

pygame.init()

# palette
black = (0, 0, 0)
white = (255, 255, 255)
skyblue = (0, 255, 255)
grey = (70, 70, 70)
fishgrey = (200, 200, 200)
fishpink = (200, 123, 123)
waterblue = (25, 85, 55)

FPS = 30
szx = 400  # 794
szy = 600  # 1123
screen = pygame.display.set_mode((szx, szy), flags=pygame.RESIZABLE)

# background
screen.fill(skyblue)
rect(screen, white, (0, int(szy/1.8), szx, szy))
line(screen, black, (0, int(szy/1.8)), (szx, int(szy/1.8)), width=1)

sun = pygame.Surface((szx, int(szy/1.8)), flags=pygame.SRCALPHA)
sun.set_alpha(100)
circle(sun, white, (szx/2, int(szy/1.8)/2), int(szy/1.8)/2, width=50)

screen.blit(sun, (0, 0))


def draw_prorub(x, y, width):
    w = int(width)
    h = int(w/2)
    prorub = pygame.Surface((w, h), flags=pygame.SRCALPHA)

    ellipse(prorub, grey, (0, 0, w, h))
    ellipse(prorub, black, (0, 0, w, h), width=1)
    ellipse(prorub, waterblue, (int(0.2 * w), int(0.2 * h), w - 2 * int(0.2 * w), h - 2 * int(0.2 * h)))
    ellipse(prorub, black, (int(0.2 * w), int(0.2 * h), w - 2 * int(0.2 * w), h - 2 * int(0.2 * h)), width=1)

    screen.blit(prorub, (x, y))


def draw_penguin(x, y, width, rot=False):
    w = width
    penguin = pygame.Surface((w, w), flags=pygame.SRCALPHA)

    line(penguin, black, (int(w / 3), int(w / 1.9)), (w, 0), width=5)
    line(penguin, black, (w, 0), (w, w), width=3)

    ellipse(penguin, white, (int(w / 5.4), int(w / 7.7), int(w / 3.8), int(w / 6.5)))  # head
    ellipse(penguin, black, (int(w / 5.4), int(w / 7.7), int(w / 3.8), int(w / 6.5)), width=1)

    ellipse(penguin, black, (int(1.8 * w / 5.4), int(1.3 * w / 7.7), 8, 8))  # eye

    ellipse(penguin, white, (int(w / 4.6), int(w / 7.2), int(w / 19.6), int(w / 25)))
    ellipse(penguin, black, (int(w / 4.6), int(w / 7.2), int(w / 19.6), int(w / 25)), width=1)

    ellipse(penguin, white, (0, w // 4, int(w / 2.5), int(w / 1.5)))  # torso
    ellipse(penguin, black, (0, w // 4, int(w / 2.5), int(w / 1.5)), width=1)

    ellipse(penguin, white, (int(w / 3), int(w / 2.5), int(w / 5.9), int(w / 10.8)))  # hand
    ellipse(penguin, black, (int(w / 3), int(w / 2.5), int(w / 5.9), int(w / 10.8)), width=1)

    ellipse(penguin, white, (int(w / 5), int(w / 1.3), int(w / 3.3), int(w / 4.3)))
    ellipse(penguin, black, (int(w / 5), int(w / 1.3), int(w / 3.3), int(w / 4.3)), width=1)

    ellipse(penguin, white, (int(w / 2.6), int(w / 1.08), int(w / 4.48), int(w / 13)))
    ellipse(penguin, black, (int(w / 2.6), int(w / 1.08), int(w / 4.48), int(w / 13)), width=1)

    if rot:
        penguin = pygame.transform.flip(penguin, True, False)

    screen.blit(penguin, (x, y))


def draw_fish(x, y, width, rot=False):
    w = int(width)
    tw = int(w * 0.1)
    fish = pygame.Surface((w, w), flags=pygame.SRCALPHA)

    ellipse(fish, fishpink, (int(w / 2.6), 0, int(w / 2.6), int(w / 3.2)))  # plavnik
    ellipse(fish, black, (int(w / 2.6), 0, int(w / 2.6), int(w / 3.2)), width=1)

    ellipse(fish, fishgrey, (-int(w / 1.3), tw, w - tw, int(w/2) - tw))  # tail
    ellipse(fish, black, (-int(w / 1.3), tw, w - tw, int(w / 2) - tw), width=1)

    ellipse(fish, fishgrey, (tw, tw, w - tw, int(w/2) - tw))  # torso
    ellipse(fish, black, (tw, tw, w - tw, int(w / 2) - tw), width=1)

    ellipse(fish, black, (int(w / 1.4), int(w * 0.2), 7, 7))  # eye

    fish = pygame.transform.rotate(fish, 10)

    if rot:
        fish = pygame.transform.flip(fish, True, False)

    screen.blit(fish, (x, y))


draw_prorub(300, 370, 100)
draw_penguin(0, 50, 350)
draw_fish(300, 470, 50)
draw_fish(330, 420, 75, True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
