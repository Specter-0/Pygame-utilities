import pygame as pg
import pgu 
pg.init()
pgu.init()

screen = pg.display.set_mode([500, 500])

class Player(pg.sprite.Sprite, pgu.utility.sprite.movement):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((25, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

player = Player()

def main(running):
    clock = pg.time.Clock()
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))

        screen.blit(player.surf, player.rect)

        pg.display.flip()

main(True)

pg.quit()
