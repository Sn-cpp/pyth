import pygame as game
import numpy as np
import math
import time
game.init()

window = game.display.set_mode((800, 600))
ticker = game.time.Clock()
points = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

v = np.array([1/2,1/2,1/2])

p_xy = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

colo = (255, 0, 0)
offset = 300
scale = 100

x_deg = 0
y_deg = 0
z_deg = 0
time.sleep(3)
while True:
    ticker.tick(20)

    r_x = np.array([
        [1, 0, 0],
        [0, math.cos(x_deg), -math.sin(x_deg)],
        [0, math.sin(x_deg), math.cos(x_deg)]
    ])
    r_y = np.array([
        [math.cos(y_deg), 0 , math.sin(y_deg)],
        [0, 1, 0],
        [-math.sin(y_deg), 0, math.cos(y_deg)]
    ])
    r_z = np.array([
        [math.cos(z_deg), -math.sin(z_deg), 0],
        [math.sin(z_deg), math.cos(z_deg), 0],
        [0, 0, 1]
    ])
    xy = []
    for i in range(0, len(points)):
        temp = points[i] - v
        temp = temp.dot(r_x)
        temp = temp.dot(r_y)
        # temp = temp.dot(r_z)
        temp = temp + v
        temp = temp.dot(p_xy)
        xy.append(temp)
    for i in range(0, len(xy)):
        game.draw.circle(window, colo, [xy[i][0]*scale + offset, xy[i][1]*scale + offset], 2)
       
    for i in range(0, len(xy) - 1):
        for j in range(1, len(xy)):
            if  
    game.display.update()

    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            game.quit()
    window.fill((0, 0, 0))
    x_deg += 0.1
    y_deg += 0.1
   