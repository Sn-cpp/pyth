import pygame as game
import numpy as np
import math
import time

game.init()

window = game.display.set_mode((800, 600))
ticker = game.time.Clock()

points = np.array([
    [0,0,0],
    [0,1,0],
    [1,1,0],
    [1,0,0],
    [0,0,1],
    [0,1,1],
    [1,1,1],
    [1,0,1]
])

O_vector = np.array([1/2, 1/2, 1/2]) 

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
mouse_x, mouse_y = 0,0
count = 0

max_deg = math.pi/3
countdown = 0
while True:
    ticker.tick(20)
    
    # keys = game.key.get_pressed()
    # if keys[game.K_w]:
    #     x_deg += 0.1
    # if keys[game.K_s]:
    #     x_deg -= 0.1
    # if keys[game.K_a]:
    #     y_deg += 0.1
    # if keys[game.K_d]:
    #     y_deg -= 0.1
    if game.mouse.get_pressed()[0] == True:
        countdown == 500
        new_x,new_y = game.mouse.get_pos()
        r = (new_x - (0.5*scale + offset))**2 + (new_y - (0.5*scale + offset))**2
        
        if r <= 100**2:
            if count == 0:
                count = 1
                mouse_x = new_x
                mouse_y = new_y
                continue
            if new_x != mouse_x:
                
                if (new_x - mouse_x) > 5 and y_deg < max_deg:
                    y_deg -= 0.1
                if (new_x - mouse_x) < 5 and y_deg > -max_deg:
                    y_deg += 0.1
                mouse_x = new_x
            if new_y != mouse_y:
                if (new_y - mouse_y) > 5 and x_deg > -max_deg:
                    x_deg += 0.1
                if (new_y - mouse_y) < 5 and y_deg < max_deg:
                    x_deg -= 0.1
                mouse_y = new_y
    else:
        if x_deg == 0 and y_deg == 0:
            count = 0
        if x_deg != 0:
            x_deg += 0.5*(0 - x_deg)
        if y_deg != 0:
            y_deg += 0.5*(0 - y_deg)
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
    
    newpoints = points - O_vector
    newpoints = newpoints.dot(r_x)
    newpoints = newpoints.dot(r_y)
    newpoints = newpoints + O_vector
    newpoints = newpoints.dot(p_xy)

    length = len(newpoints)
    game.draw.circle(window, (255, 255, 255), [0.5*scale + offset, 0.5*scale + offset],2)
    for i in range(0, length):
        game.draw.circle(window, colo, [newpoints[i][0]*scale + offset, newpoints[i][1]*scale + offset], 5)
    
    half_length = int(length/2)
    for i in range(0, half_length):
        game.draw.aaline(window, colo, [newpoints[i][0]*scale + offset, newpoints[i][1]*scale + offset], [newpoints[(i+1) % half_length][0]*scale + offset, newpoints[(i+1) % half_length][1]*scale + offset])
        game.draw.aaline(window, colo, [newpoints[i+half_length][0]*scale + offset, newpoints[i+half_length][1]*scale + offset], [newpoints[(i+1) % half_length + half_length][0]*scale + offset, newpoints[(i+1) % half_length + half_length][1]*scale + offset])
        game.draw.aaline(window, colo, [newpoints[i+half_length][0]*scale + offset, newpoints[i+half_length][1]*scale + offset], [newpoints[(i+half_length) % half_length][0]*scale + offset, newpoints[(i+half_length) % half_length][1]*scale + offset])

    game.display.update()
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            game.quit()
    window.fill((0, 0, 0))
    if countdown > 0:
        countdown -= 1
