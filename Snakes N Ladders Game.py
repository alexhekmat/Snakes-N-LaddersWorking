import pygame
from random import randint
import time

clock = pygame.time.Clock()

pygame.init()
w = 1366
h = 768

GD = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
pygame.display.set_caption("Trouble")
pygame.display.update()
# test
# Graphics:
black = (10, 10, 10)
white = (250, 250, 250)
red = (200, 0, 0)
b_red = (240, 0, 0)
green = (0, 200, 0)
b_green = (0, 230, 0)
blue = (0, 0, 200)
grey = (50, 50, 50)
yellow = (150, 150, 0)
purple = (43, 3, 132)
b_purple = (60, 0, 190)

board = pygame.image.load("Trouble-Bigger.jpg")
die1 = pygame.image.load("Die1.png")
die2 = pygame.image.load("Die2.png")
die3 = pygame.image.load("Die3.png")
die4 = pygame.image.load("Die4.png")
die5 = pygame.image.load("Die5.png")
die6 = pygame.image.load("Die6.png")

redgoti = pygame.image.load("redgoti.png")
yellowgoti = pygame.image.load("yellowgoti.png")
greengoti = pygame.image.load("greengoti.png")
bluegoti = pygame.image.load("bluegoti.png")
menubg = pygame.image.load("menu.jpg")
p = pygame.image.load("playbg.jpg")
intbg = pygame.image.load("intropic.png")
intbg2 = pygame.image.load("intropic2.jpg")
intbg3 = pygame.image.load("intropic3.jpg")
intbg4 = pygame.image.load("intropic4.jpg")
intbg5 = pygame.image.load("intropic5.jpg")

pygame.mixer.music.load("music.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")

# mouse pos
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


# Message displaying for buttons
def message_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


# Message displaying for field
def message_display1(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)


def text_objects1(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


# Goti movement function
def goti_red1(a):
    l1 = [[814, 594], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515],
          [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152],
          [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421],
          [877, 468], [853, 514], [815, 515], [790, 490], [763, 465], [737, 437]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_red2(a):
    l1 = [[846, 573], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515],
          [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152],
          [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421],
          [877, 468], [853, 514], [815, 515], [790, 490], [763, 465]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_red3(a):
    l1 = [[871, 547], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515],
          [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152],
          [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421],
          [877, 468], [853, 514], [815, 515], [790, 490]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_red4(a):
    l1 = [[891, 513], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515],
          [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152],
          [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421],
          [877, 468], [853, 514], [815, 515]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_yellow1(a):
    l1 = [[524, 147], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225],
          [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589],
          [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320],
          [460, 270], [487, 227], [518, 223], [547, 250], [574, 276], [601, 303]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_yellow2(a):
    l1 = [[491, 167], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225],
          [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589],
          [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320],
          [460, 270], [487, 227], [518, 223], [547, 250], [574, 276]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_yellow3(a):
    l1 = [[464, 194], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225],
          [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589],
          [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320],
          [460, 270], [487, 227], [518, 223], [547, 250]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_yellow4(a):
    l1 = [[446, 226], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225],
          [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589],
          [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320],
          [460, 270], [487, 227], [518, 223]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_green1(a):
    l1 = [[445, 514], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185],
          [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318],
          [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589],
          [569, 580], [525, 557], [520, 517], [547, 492], [572, 466], [600, 439]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_green2(a):
    l1 = [[465, 514], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185],
          [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318],
          [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589],
          [569, 580], [525, 557], [520, 517], [547, 492], [572, 466]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_green3(a):
    l1 = [[491, 577], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185],
          [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318],
          [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589],
          [569, 580], [525, 557], [520, 517], [547, 492]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_green4(a):
    l1 = [[523, 594], [484, 515], [458, 470], [451, 422], [452, 371], [449, 320], [460, 270], [485, 227], [524, 185],
          [568, 161], [617, 152], [669, 152], [720, 152], [769, 160], [812, 186], [853, 225], [877, 270], [887, 318],
          [887, 370], [887, 421], [877, 468], [853, 514], [812, 554], [769, 580], [720, 589], [669, 589], [617, 589],
          [569, 580], [525, 557], [520, 517]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_blue1(a):
    l1 = [[892, 226], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554],
          [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422],
          [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152],
          [769, 160], [812, 186], [815, 223], [790, 249], [762, 276], [736, 302]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_blue2(a):
    l1 = [[871, 193], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554],
          [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422],
          [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152],
          [769, 160], [812, 186], [815, 223], [790, 249], [762, 276]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_blue3(a):
    l1 = [[845, 166], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554],
          [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422],
          [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152],
          [769, 160], [812, 186], [815, 223], [790, 249]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def goti_blue4(a):
    l1 = [[812, 147], [853, 225], [877, 270], [887, 318], [887, 370], [887, 421], [877, 468], [853, 514], [812, 554],
          [769, 580], [720, 589], [669, 589], [617, 589], [569, 580], [525, 557], [484, 515], [458, 470], [451, 422],
          [452, 371], [449, 320], [460, 270], [485, 227], [524, 185], [568, 161], [617, 152], [669, 152], [720, 152],
          [769, 160], [812, 186], [815, 223]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def text_objects1(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def dice(a):
    if a == 1:
        a = die1
    elif a == 2:
        a = die2
    elif a == 3:
        a = die3
    elif a == 4:
        a = die4
    elif a == 5:
        a = die5
    elif a == 6:
        a = die6

    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        GD.blit(a, (410, 90))
        pygame.display.update()

    # for mute and unmute


def button2(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    # mouse pos
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


# Buttons for playing:
def button1(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    # mouse pos
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


# Turn
def turn_goti1(score):
    a = randint(1, 6)  # player dice roll
    if a == 6:
        six = True
    else:
        six = False
    dice(a)
    if score + a < 33:
        if score == 0:
            if a == 6:
                score += 1
        else:
            score += a
    return score, six


def turn_goti2(score):
    a = randint(1, 6)  # player dice roll
    if a == 6:
        six = True
    else:
        six = False
    dice(a)
    if score + a < 32:
        if score == 0:
            if a == 6:
                score += 1
        else:
            score += a
    return score, six


def turn_goti3(score):
    a = randint(1, 6)  # player dice roll
    if a == 6:
        six = True
    else:
        six = False
    dice(a)
    if score + a < 31:
        if score == 0:
            if a == 6:
                score += 1
        else:
            score += a
    return score, six


def turn_goti4(score):
    a = randint(1, 6)  # player dice roll
    if a == 6:
        six = True
    else:
        six = False
    dice(a)
    if score + a < 30:
        if score == 0:
            if a == 6:
                score += 1
        else:
            score += a
    return score, six


# Quitting:
def Quit():
    pygame.quit()
    quit()


# Buttons:
def button(text, xmouse, ymouse, x, y, w, h, i, a, fs, b):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1:
                options()
            elif b == 5:
                return 5
            elif b == 0:
                Quit()
            elif b == "s" or b == 2 or b == 3 or b == 4:
                return b
            elif b == 7:
                options()
            else:
                return True






    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


# def pause():
# j=True
# while j:
# mouse pos
# mouse=pygame.mouse.get_pos()
# click=pygame.mouse.get_pressed()
# GD.blit(pause_bg,(0,0))
# mouse=pygame.mouse.get_pos()
# click=pygame.mouse.get_pressed()
# if button("Resume",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,10):
# j=False
# if button("Main Menu",mouse[0],mouse[1],(w/2)-150,500,300,50,red,b_red,30,10):
# main()
# pygame.display.update()

def intro():
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        GD.blit(intbg, (0, 0))
        pygame.display.update()
    while True:
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg2, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg3, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg4, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg5, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()


# Main Menu
def main():
    pygame.mixer.music.play(-1)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        GD.blit(menubg, (0, 0))
        button("Play", mouse[0], mouse[1], (w / 2 - 100), h / 2, 200, 100, green, b_green, 60, 1)

        button("Quit", mouse[0], mouse[1], (w / 2 - 100), (h / 2) + 200, 200, 100, red, b_red, 60, 0)

        mouse = pygame.mouse.get_pos()
        if button2("Mute Music", mouse[0], mouse[1], 1166, 0, 200, 50, purple, b_purple, 25):
            pygame.mixer.music.pause()
        if button2("Play Music", mouse[0], mouse[1], 1166, 75, 200, 50, purple, b_purple, 25):
            pygame.mixer.music.unpause()

        pygame.display.update()


# Options Menu:
def options():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        b1 = b2 = b3 = b4 = b5 = -1
        GD.blit(menubg, (0, 0))
        # Single player button
        b1 = button("1 Player", mouse[0], mouse[1], (w / 2 - 150), 250, 300, 50, green, b_green, 30, "s")
        # 2 player button
        b2 = button("2 Players", mouse[0], mouse[1], (w / 2) - 150, 350, 300, 50, green, b_green, 30, 2)
        # 3 player
        b3 = button("3 Players", mouse[0], mouse[1], (w / 2) - 150, 450, 300, 50, green, b_green, 30, 3)
        # 4 player
        b4 = button("4 Players", mouse[0], mouse[1], (w / 2) - 150, 550, 300, 50, green, b_green, 30, 4)
        # Back button
        b5 = button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red, b_red, 30, 5)
        if b5 == 5:
            main()
        if b1 == "s":
            play(21)
        if b2 == 2:
            play(2)
        if b3 == 3:
            play(3)
        if b4 == 4:
            play(4)

        pygame.display.update()


# play function
def play(b):
    b6 = -1
    time = 3000
    if b6 == 7:
        options()
    GD.blit(p, (0, 0))
    GD.blit(board, (w / 2 - 250, h / 2 - 250))

    ##Red Homes
    xcr = 814
    ycr = 594
    xcr1 = 846
    ycr1 = 573
    xcr2 = 871
    ycr2 = 547
    xcr3 = 891
    ycr3 = 513

    ##Green Homes

    xcg = 445
    ycg = 514
    xcg1 = 465
    ycg1 = 549
    xcg2 = 491
    ycg2 = 577
    xcg3 = 523
    ycg3 = 594

    ##Yellow Homes

    xcy = 524
    ycy = 147
    xcy1 = 491
    ycy1 = 167
    xcy2 = 464
    ycy2 = 194
    xcy3 = 446
    ycy3 = 226

    ##Blue homes

    xcb = 892
    ycb = 226
    xcb1 = 871
    ycb1 = 193
    xcb2 = 845
    ycb2 = 166
    xcb3 = 812
    ycb3 = 147

    GD.blit(redgoti, (xcr, ycr))
    GD.blit(redgoti, (xcr1, ycr1))
    GD.blit(redgoti, (xcr2, ycr2))
    GD.blit(redgoti, (xcr3, ycr3))
    if 5 > b > 1 or b == 21:
        GD.blit(yellowgoti, (xcy, ycy))
        GD.blit(yellowgoti, (xcy1, ycy1))
        GD.blit(yellowgoti, (xcy2, ycy2))
        GD.blit(yellowgoti, (xcy3, ycy3))
    if 5 > b > 2 or b == 21:
        GD.blit(greengoti, (xcg, ycg))
        GD.blit(greengoti, (xcg1, ycg1))
        GD.blit(greengoti, (xcg2, ycg2))
        GD.blit(greengoti, (xcg3, ycg3))
    if 5 > b > 2:
        GD.blit(bluegoti, (xcb, ycb))
        GD.blit(bluegoti, (xcb1, ycb1))
        GD.blit(bluegoti, (xcb2, ycb2))
        GD.blit(bluegoti, (xcb3, ycb3))
    p1 = "Player 1"
    p1score1 = 0
    p1score2 = 0
    p1score3 = 0
    p1score4 = 0
    if b == 21:
        p2 = "Computer"
        p2score1 = 0
        p2score2 = 0
        p2score3 = 0
        p2score4 = 0
    if 5 > b > 1:
        p2 = "Player 2"
        p2score1 = 0
        p2score2 = 0
        p2score3 = 0
        p2score4 = 0
    if 5 > b > 2:
        p3 = "Player 3"
        p3score1 = 0
        p3score2 = 0
        p3score3 = 0
        p3score4 = 0
    if 5 > b > 3:
        p4 = "Player 4"
        p4score1 = 0
        p4score2 = 0
        p4score3 = 0
        p4score4 = 0
    t = 1
    play = True
    while True:
        l = False
        s = False
        time = 3000
        GD.blit(p, (0, 0))
        GD.blit(board, (w / 2 - 250, h / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        if b == 21:
            # (player,score,text,xmouse,ymouse,x,y,w,h,i,a,fs)

            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red, grey, 30):
                if t == 1:
                    if p1score1 < 32:
                        p1score1, six = turn_goti1(p1score1)
                        if not six:
                            t += 1
                        xcr, ycr = goti_red1(p1score1)
                    elif p1score2 < 31:
                        p1score2, six = turn_goti2(p1score2)
                        if not six:
                            t += 1
                        xcr1, ycr1 = goti_red2(p1score2)
                    elif p1score3 < 30:
                        p1score3, six = turn_goti3(p1score3)
                        if not six:
                            t += 1
                        xcr2, ycr2 = goti_red3(p1score3)
                    else:
                        p1score4, six = turn_goti4(p1score4)
                        if not six:
                            t += 1
                        xcr3, ycr3 = goti_red4(p1score4)
                        if p1score4 == 29:
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()




            button1("Computer", mouse[0], mouse[1], 400, 700, 200, 50, yellow, grey, 30)
            if True:
                if t == 2:
                    if p2score1 < 32:
                        p2score1, six = turn_goti1(p2score1)
                        xcy, ycy = goti_yellow1(p2score1)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                    elif p2score2 < 31:
                        p2score2, six = turn_goti2(p2score2)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                        xcy1, ycy1 = goti_yellow2(p2score2)
                    elif p2score3 < 30:
                        p2score3, six = turn_goti3(p2score3)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                        xcy2, ycy2 = goti_yellow3(p2score3)
                    else:
                        p2score4, six = turn_goti4(p2score4)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                        xcy3, ycy3 = goti_yellow4(p2score4)
                        if p2score4 == 29:
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()



        if 5 > b > 1:
            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red, grey, 30):
                if t == 1:
                    if p1score1 < 32:
                        p1score1, six = turn_goti1(p1score1)
                        if not six:
                            t += 1
                        xcr, ycr = goti_red1(p1score1)
                    elif p1score2 < 31:
                        p1score2, six = turn_goti2(p1score2)
                        if not six:
                            t += 1
                        xcr1, ycr1 = goti_red2(p1score2)
                    elif p1score3 < 30:
                        p1score3, six = turn_goti3(p1score3)
                        if not six:
                            t += 1
                        xcr2, ycr2 = goti_red3(p1score3)
                    else:
                        p1score4, six = turn_goti4(p1score4)
                        if not six:
                            t += 1
                        xcr3, ycr3 = goti_red4(p1score4)
                        if p1score4 == 29:
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()


            if button1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, yellow, grey, 30):
                if t == 2:
                    if p2score1 < 32:
                        p2score1, six = turn_goti1(p2score1)
                        xcy, ycy = goti_yellow1(p2score1)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                    elif p2score2 < 31:
                        p2score2, six = turn_goti2(p2score2)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                        xcy1, ycy1 = goti_yellow2(p2score2)
                    elif p2score3 < 30:
                        p2score3, six = turn_goti3(p2score3)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                        xcy2, ycy2 = goti_yellow3(p2score3)
                    else:
                        p2score4, six = turn_goti4(p2score4)
                        if not six:
                            t += 1
                            if b < 3 or b == 21:
                                t = 1
                        xcy3, ycy3 = goti_yellow4(p2score4)
                        if p2score4 == 29:
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()

        if 5 > b > 2:
            if button1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, green, grey, 30):
                if t == 3:
                    if p3score1 < 32:
                        p3score1, six = turn_goti1(p3score1)
                        xcg, ycg = goti_green1(p3score1)
                        if not six:
                            t += 1
                            if b < 4:
                                t = 1
                    elif p3score2 < 31:
                        p3score2, six = turn_goti2(p3score2)
                        if not six:
                            t += 1
                            if b < 4:
                                t = 1
                        xcg1, ycg1 = goti_green2(p3score2)
                    elif p3score3 < 30:
                        p3score3, six = turn_goti3(p3score3)
                        if not six:
                            t += 1
                            if b < 4:
                                t = 1
                        xcg2, ycg2 = goti_green3(p3score3)
                    else:
                        p3score4, six = turn_goti4(p3score4)
                        if not six:
                            t += 1
                            if b < 4:
                                t = 1
                        xcg3, ycg3 = goti_green4(p3score4)
                        if p3score4 == 29:
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()

        if 5 > b > 3:
            if button1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, blue, grey, 30):
                if t == 4:
                    if p4score1 < 32:
                        p4score1, six = turn_goti1(p4score1)
                        xcb, ycb = goti_blue1(p4score1)
                        if not six:
                            t += 1
                            if b < 5:
                                t = 1

                    elif p4score2 < 31:
                        p4score2, six = turn_goti2(p4score2)
                        if not six:
                            t += 1
                            if b < 5:
                                t = 1
                        xcb1, ycb1 = goti_blue2(p4score2)
                    elif p4score3 < 30:
                        p4score3, six = turn_goti3(p4score3)
                        if not six:
                            t += 1
                            if b < 5:
                                t = 1
                        xcb2, ycb2 = goti_blue3(p4score3)
                    else:
                        p4score4, six = turn_goti4(p4score4)
                        if not six:
                            t += 1
                            if b < 5:
                                t = 1
                        xcb3, ycb3 = goti_blue4(p4score4)
                        if p4score4 == 29:
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()

        b6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, red, b_red, 30, 7)
        GD.blit(redgoti, (xcr, ycr))
        GD.blit(redgoti, (xcr1, ycr1))
        GD.blit(redgoti, (xcr2, ycr2))
        GD.blit(redgoti, (xcr3, ycr3))
        if 5 > b > 1 or b == 21:
            GD.blit(yellowgoti, (xcy, ycy))
            GD.blit(yellowgoti, (xcy1, ycy1))
            GD.blit(yellowgoti, (xcy2, ycy2))
            GD.blit(yellowgoti, (xcy3, ycy3))

        if 5 > b > 2:
            GD.blit(greengoti, (xcg, ycg))
            GD.blit(greengoti, (xcg1, ycg1))
            GD.blit(greengoti, (xcg2, ycg2))
            GD.blit(greengoti, (xcg3, ycg3))

        if 5 > b > 3:
            GD.blit(bluegoti, (xcb, ycb))
            GD.blit(bluegoti, (xcb1, ycb1))
            GD.blit(bluegoti, (xcb2, ycb2))
            GD.blit(bluegoti, (xcb3, ycb3))

        clock.tick(7)
        pygame.display.update()


intro()
main()
