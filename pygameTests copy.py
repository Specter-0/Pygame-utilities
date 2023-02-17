import pygame as pg
import pgu
import math
pg.init()
pgu.init()

width = 1350
height = 800
win = pg.display.set_mode([width, height])
pgu.utility.gravity_set_values(200)
pgu.utility.gravity_set_timestep(3600*24)

def main(running):
    clock = pg.time.Clock()

    sun = pgu.utility.Gravity(0, 0, 0, 30, 1.98892 * 10**30, pgu.YELLOW) #1.98892 * 10**30

    earth = pgu.utility.Gravity(-1, 0, 29.783 * 1000, 16, 6.9742 * 10**24, pgu.BLUE) #6.9742 * 10**24

    mars = pgu.utility.Gravity(-1.524, 0, 24.077 * 1000, 12, 6.39 * 10**23, pgu.DARKRED) #6.39 * 10**23

    mercury = pgu.utility.Gravity(-0.387, 0, 47.4 * 1000, 8, 0.330 * 10**24, pgu.GRAY) #0.330 * 10**24

    venus = pgu.utility.Gravity(-0.723, 0, 35.02 * 1000, 14, 1.8685 * 10**24, pgu.ORANGE) #1.8685 * 10**24

    moon = pgu.utility.Gravity(-1.1, 0, 1.022 * 1000, 1, 7.342 * 10**22, pgu.WHITE)

    objects = [sun, earth, mars, mercury, venus, moon]

    for object in objects:
        object.path_track()

    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
 
        win.fill((pgu.BLACK))

        for object in objects:
            object.update_pos(objects)
            object.draw(win, width, height)
            object.draw_path(win, width, height)
            #object.draw_path(win, width, height)

        pg.display.flip()   

main(True)

pg.quit()
