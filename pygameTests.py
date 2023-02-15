import pygame as pg
import pgu 
import math
pg.init()
pgu.init()



width = 1350
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
        y = self.y * self.SCALE + height / 2
        pg.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance
        
        force = self.G * self.mass * other.mass /distance**2
        v = math.atan2(distance_y, distance_x)
        force_x = math.cos(v) * force
        force_y = math.sin(v) * force
        return force_x, force_y
    
    def update_pos(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))



def main(running):
    clock = pg.time.Clock()

    sun = Planet(0, 0, 30, pgu.YELLOW, 1.98892 * 10**30) #1.98892 * 10**30
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, pgu.BLUE, 6.9742 * 10**24) #6.9742 * 10**24
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, pgu.RED, 6.39 * 10**23) #6.39 * 10**23
    mars.y_vel = 24.077 * 1000

    mercury = Planet(-0.387 * Planet.AU, 0, 8, pgu.GRAY, 0.330 * 10**24) #0.330 * 10**24
    mercury.y_vel = 47.4 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 14, pgu.WHITE, 1.8685 * 10**24) #1.8685 * 10**24
    venus.y_vel = 35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        win.fill((pgu.BLACK))

        for planet in planets:
            planet.update_pos(planets)
            planet.draw(win)

        pg.display.flip()   

main(True)

pg.quit()
