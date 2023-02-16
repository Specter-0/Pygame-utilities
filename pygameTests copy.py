import pygame as pg
import pgu
import math
pg.init()
pgu.init()

width = 1350
height = 800
win = pg.display.set_mode([width, height])
pgu.utility.gravity_set_values(149.6e6 * 1000, 200, 3600*30)

def main(running):
    clock = pg.time.Clock()

    sun = pgu.utility.gravity_create_object(0, 0, 30, 1.98892 * 10**30, pgu.YELLOW) #1.98892 * 10**30

    earth = pgu.utility.gravity_create_object(-1, 0, 16, 6.9742 * 10**24) #6.9742 * 10**24
    earth.y_vel = 29.783 * 1000

    mars = pgu.utility.gravity_create_object(-1.524, 0, 12, 6.39 * 10**23) #6.39 * 10**23
    mars.y_vel = 24.077 * 1000

    mercury = pgu.utility.gravity_create_object(-0.387, 0, 8, 0.330 * 10**24) #0.330 * 10**24
    mercury.y_vel = 47.4 * 1000

    venus = pgu.utility.gravity_create_object(-0.723, 0, 14, 1.8685 * 10**24) #1.8685 * 10**24
    venus.y_vel = 35.02 * 1000

    objects = [sun, earth, mars, mercury, venus]

    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        win.fill((pgu.BLACK))

        for object in objects:
            object.update_pos(objects)
            object.draw(win, width, height)

        pg.display.flip()   

main(True)

pg.quit()
