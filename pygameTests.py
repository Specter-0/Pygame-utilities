import pygame as pg
import pgu 
pg.init()
pgu.init()



width = 800
height = 800
win = pg.display.set_mode([width, height])

class Planet(pg.sprite.Sprite, pgu.utility.sprite.movement):
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1AU = 100px
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y 
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.y_vel = 0
        self.x_vel = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + width / 2
        y = self.x * self.SCALE + height / 2
        pg.draw.circle(win, self.color, (x, y), self.radius)

def main(running):
    clock = pg.time.Clock()

    sun = Planet(0, 0, 30, pgu.YELLOW, 1.98892 * 10**30, )
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, pgu.BLUE, 5.9742 * 10*24)

    mars = Planet(-1.524 * Planet.AU, 0, 12, pgu.RED, 6.39 * 10**23)

    mercury = Planet(-0.387 * Planet.AU, 0, 8, pgu.GRAY, 0.330 * 10**24)

    venus = Planet(-0.723 * Planet.AU, 0, 14, pgu.WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        win.fill((pgu.BLACK))

        for planet in planets:
            planet.draw(win)

        pg.display.flip()   

main(True)

pg.quit()
