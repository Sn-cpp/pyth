import pygame as eg
import time
import random
clock = eg.time.Clock()
eg.init()

window = eg.display.set_mode((720,540))
running = True
rectangle = eg.draw.rect(window, (100,100,100), [50,50,50,50], 2)
    
def user_Input():
    x,y = 0,0
    keys = eg.key.get_pressed()
    if keys[eg.K_w]:
        y = -1
    # keys = eg.key.get_pressed()
    if keys[eg.K_s]:
        y = 1
    # keys = eg.key.get_pressed()
    if keys[eg.K_d]:
        x = 1
    # keys = eg.key.get_pressed()
    if keys[eg.K_a]:
        x = -1
    if x != 0 or y != 0:
        change = True
    else:
        change = False
    return (change, x, y)
def hit(target,proj):
    if len(target) > 0 and len(proj) > 0:
        for i in target:
            for j in proj:
                collide = eg.Rect.colliderect(i, j)
                if collide == True:
                    eg.draw.rect(window, (0,0,0), i)
                    eg.draw.rect(window, (0,0,0), j)
                    eg.display.update()
                    return target.index(i),proj.index(j)
    return None
delay = 0
delay2 = 0
proj = []
target = []
while running:
    clock.tick(500)
    rx = rectangle.x + 50
    ry = rectangle.y + 25

    command,x,y = user_Input()
    if command == True:
        rectangle.move_ip(x, y)
        
    key = eg.key.get_pressed()
    if key[eg.K_f]:
        if delay == 0:
            proj.append(eg.draw.rect(window, (255, 0, 0), [rx, ry, 20, 10], 2))
            delay = 50
    key = eg.key.get_pressed()
    if key[eg.K_e]:
        target.append(eg.draw.rect(window, (255, 255, 255), [600, 400, 50, 50],2))
        delay2 = 50
    for event in eg.event.get():
        if event.type == eg.QUIT:
            proj.clear()
            running = False

    window.fill((0, 0, 0))
    eg.draw.rect(window, (100, 100, 100), rectangle)


    if len(proj) != 0:
        for i in proj:
            if i.x > 0 and i.x < 720:
                i.x += 1
                eg.draw.rect(window, (255, 0, 0), i)
            else:
                proj.pop(proj.index(i))
    for i in target:
        eg.draw.rect(window, (255, 255, 255), i)
    eg.display.update()

    if delay > 0:
        delay -= 1
    if delay2 >0:
        delay2 -= 1
    


