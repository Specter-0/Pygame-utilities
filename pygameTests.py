import pygame as pg
import pgu 
pg.init()
pgu.init()

screen = pg.display.set_mode([800, 800])

class Planet(pg.sprite.Sprite, pgu.utility.sprite.movement):
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1AU = 100px
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        super(Planet, self).__init__()
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




        self.rect = self.surf.get_rect()


player = Planet()

def main(running):
    clock = pg.time.Clock()
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((pgu.WHITE))

        screen.blit(player.surf, player.rect)

        pg.display.flip()

main(True)

pg.quit()
