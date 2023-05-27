import pygame as pg

def drawSky(window, color, skyline_y, window_width):
    window.fill(color, [0, 0, window_width, skyline_y])
def drawGround(window, color, skyline_y, window_width, window_height):
    window.fill(color, [0, window_height - skyline_y, window_width, window_height - skyline_y])
def updateScreen(window):
    window.fill((0, 0, 0))











pg.init()

window_width = 640
window_height = 480
window = pg.display.set_mode((window_width, window_height))

ground_color = (0, 0, 100)
sky_color = (0, 0, 0)
skyline_pos = 200
change = True

eye_start = (0, 0)
camera_plane = (0, 1)

while True:
    if change == True:
        change = False
        updateScreen(window)
        drawSky(window, sky_color, skyline_pos, window_width)
        drawGround(window, ground_color, skyline_pos, window_width, window_height)
        pg.display.update()

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
    
    