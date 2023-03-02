import pygame as pg
import pgu
import math
pg.init()
pgu.init()

width = 1350
height = 800
win = pg.display.set_mode([width, height])
pgu.utility.Gravity.set_values(100) #sette globale verider for Gravity klassen
pgu.utility.Gravity.set_timestep(3600*24) #sette timestep

#main loop
def main(running):
    clock = pg.time.Clock() #del en av fps limit

    # lager Gravity objekter
    sun = pgu.utility.Gravity(0, 0, 0, 30, 1.98892 * 10**30, pgu.YELLOW) #1.98892 * 10**30

    earth = pgu.utility.Gravity(-1, 0, 29.783 * 1000, 16, 6.9742 * 10**24, pgu.BLUE) #6.9742 * 10**24

    mars = pgu.utility.Gravity(-1.524, 0, 24.077 * 1000, 12, 6.39 * 10**24, pgu.DARKRED) #6.39 * 10**23

    mercury = pgu.utility.Gravity(-0.387, 0, 47.4 * 1000, 8, 0.330 * 10**24, pgu.GRAY) #0.330 * 10**24

    venus = pgu.utility.Gravity(-0.723, 0, 35.02 * 1000, 14, 1.8685 * 10**24, pgu.ORANGE) #1.8685 * 10**24

    jupiter = pgu.utility.Gravity(-5.2, 0, 13.1 * 1000, 20, 1898 * 10**24, pgu.RED)

    objects = [sun, earth, mars, mercury, venus, jupiter]

    for object in objects:
        object.path_track() #skrur på path_tracking for alle objektene i objekts

    while running:
        clock.tick(144) # fps cap
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
 
        win.fill((pgu.BLACK))

        for object in objects: #opptaterer og tegner objektene på skjermen
            object.update_pos(objects)
            object.draw(win, width, height)
            object.draw_path(win, width, height)

        pg.display.flip()   

main(True)

pg.quit()
